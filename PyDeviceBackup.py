# PyDeviceBackup.py, licensed under the MIT license
# Copyright 2024 NinjaCheetah

import sys
import os
import time
import pathlib
import platform

from pymobiledevice3 import lockdown
from pymobiledevice3 import usbmux
from pymobiledevice3.services import mobilebackup2
from pymobiledevice3.exceptions import *

from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTreeWidgetItem, QHeaderView, QStyle,
                               QStyleFactory, QFileDialog)
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject

from qt.py.ui_MainMenu import Ui_MainWindow


# Signals needed for the worker used for threading the downloads.
class WorkerSignals(QObject):
    result = Signal(int)
    progress = Signal(int)


# Worker class used to thread the downloads.
class Worker(QRunnable):
    def __init__(self, fn, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        # All possible errors *should* be caught by the code and will safely return specific error codes. In the
        # unlikely event that an unexpected error happens, it can only possibly be a ValueError, so handle that and
        # return code 1.
        try:
            result = self.fn(**self.kwargs)
        except ValueError:
            self.signals.result.emit(1)
        else:
            self.signals.result.emit(result)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.log_text = ""
        self.lockdown_client = None
        self.active_device_udid = ""
        self.threadpool = QThreadPool()
        self.ui.start_backup_btn.clicked.connect(self.start_backup_btn_pressed)
        self.ui.start_restore_btn.clicked.connect(self.start_restore_btn_pressed)
        self.ui.choose_backup_dir_btn.clicked.connect(self.choose_backup_dir_btn_pressed)
        device_listener = Worker(self.watch_for_device)
        device_listener.signals.result.connect(self.new_device_connected)
        self.threadpool.start(device_listener)

    def watch_for_device(self, progress_callback):
        device_list = None
        while device_list is None or len(device_list) == 0:
            try:
                device_list = usbmux.list_devices()
            except ConnectionFailedToUsbmuxdError:
                time.sleep(1)
        print(device_list)
        self.active_device_udid = device_list[0].serial
        return 0

    def new_device_connected(self):
        self.lockdown_client = lockdown.create_using_usbmux(serial=self.active_device_udid)
        print("Found new device: " + self.active_device_udid)
        self.ui.device_name_lbl.setText(self.lockdown_client.all_values.get("DeviceName"))
        self.ui.device_type_lbl.setText(self.lockdown_client.display_name)
        self.ui.ios_version_lbl.setText("iOS Version: " + self.lockdown_client.product_version)
        self.ui.device_udid_lbl.setText("UDID: " + self.lockdown_client.identifier)
        print(self.lockdown_client.short_info)
        # Issue device disconnect listener.
        disconnect_listener = Worker(self.watch_for_disconnect)
        disconnect_listener.signals.result.connect(self.device_disconnected)
        self.threadpool.start(disconnect_listener)

    def watch_for_disconnect(self, progress_callback):
        device_connected = True
        while device_connected:
            try:
                date = self.lockdown_client.date
                time.sleep(1)
            except ConnectionFailedToUsbmuxdError:
                device_connected = False
        return 0

    def device_disconnected(self):
        self.lockdown_client = None
        self.ui.device_name_lbl.setText("No Device Connected")
        self.ui.device_type_lbl.setText("Connect a device to begin")
        self.ui.ios_version_lbl.setText("iOS Version: ")
        self.ui.device_udid_lbl.setText("UDID: ")
        # Reissue device connection listener.
        device_listener = Worker(self.watch_for_device)
        device_listener.signals.result.connect(self.new_device_connected)
        self.threadpool.start(device_listener)

    def start_backup_btn_pressed(self):
        msg_box = QMessageBox()
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        # Make sure the provided directory exists before we begin.
        backup_dir = pathlib.Path(self.ui.backup_dir_entry.text())
        if not backup_dir.is_dir():
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowTitle("Backup Directory Not Found")
            msg_box.setText("The specified backup directory does not exist!")
            msg_box.setInformativeText("Please ensure that the directory you've specified exists and can be written to"
                                       ".")
            msg_box.exec()
            return
        # Make sure that there's an active lockdown client connected.
        if self.lockdown_client is None:
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowTitle("No Device Connected")
            msg_box.setText("No device is connected to back up!")
            msg_box.setInformativeText("Please ensure that your device is connected and is recognized by the app before"
                                       " trying to begin the backup.")
            msg_box.exec()
            print("No device is connected!")
            return
        # We're good to do, so lock the UI.
        self.ui.start_backup_btn.setEnabled(False)
        self.ui.start_restore_btn.setEnabled(False)
        self.ui.status_lbl.setText("Preparing backup... please wait")
        # Create new thread worker to handle the backup operation.
        worker = Worker(self.run_backup, backup_dir=backup_dir)
        worker.signals.result.connect(self.result_handler)
        worker.signals.progress.connect(self.progress_handler)
        self.threadpool.start(worker)

    def start_restore_btn_pressed(self):
        #lockdown_client = lockdown.create_using_usbmux()
        #print(lockdown_client.identifier)
        print(self.watch_for_device())

    def run_backup(self, progress_callback, backup_dir: pathlib.Path):
        # Create a mobilebackup2service instance using the provided lockdown client, so we can start the backup.
        backup_service = mobilebackup2.Mobilebackup2Service(self.lockdown_client)
        # Determine if we need to do a full backup or just a diff backup.
        device_dir = backup_dir.joinpath(self.lockdown_client.identifier)
        if device_dir.is_dir() and pathlib.Path(device_dir.joinpath("Manifest.db")).exists():
            full_backup = False
            print("Existing backup found for device with UUID \"" + self.lockdown_client.identifier + "\". Performing "
                  "diff backup.")
        else:
            full_backup = True
            print("No pre-existing backup found for device with UUID \"" + self.lockdown_client.identifier + "\". "
                  " Performing full backup.")
        try:
            backup_service.backup(backup_directory=backup_dir, progress_callback=progress_callback.emit,
                                  full=full_backup)
        except BrokenPipeError:
            print("Lost connection to device!")
            return -1
        else:
            backup_service.close()
            return 0

    def result_handler(self, result):
        # Handle all possible error codes returned from backup/restore processes.
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        if result == 0:
            self.ui.status_lbl.setText("Backup Complete!")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("Backup Completed")
            msg_box.setText("Backup was successfully completed!")
            msg_box.setInformativeText("You may now disconnect your device.")
            msg_box.exec()
        elif result == -1:
            msg_box.setWindowTitle("Device Disconnected")
            msg_box.setText("PyDeviceBackup has lost connection to your device.")
            msg_box.setInformativeText("Please reconnect your device, and ensure that it remains connected throughout"
                                       " the entire backup.")
            msg_box.exec()
        # Unlock UI again.
        self.ui.start_backup_btn.setEnabled(True)
        self.ui.start_restore_btn.setEnabled(True)

    def progress_handler(self, progress):
        if progress > 0:
            self.ui.status_lbl.setText("Backup in progress... please wait")
        self.ui.progress_bar.setValue(progress)

    def choose_backup_dir_btn_pressed(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.Directory)
        if file_dialog.exec():
            backup_dir_path = file_dialog.selectedFiles()[0]
            self.ui.backup_dir_entry.setText(backup_dir_path)
            print(backup_dir_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load the system plugins directory on Linux for system styles, if it exists. Try using Breeze if available, because
    # it looks nice, but fallback on kvantum if it isn't, since kvantum is likely to exist. If all else fails, fusion.
    if platform.system() == "Linux":
        if os.path.isdir("/usr/lib/qt6/plugins"):
            app.addLibraryPath("/usr/lib/qt6/plugins")
            if "Breeze" in QStyleFactory.keys():
                app.setStyle(QStyleFactory.create("breeze"))
            elif "kvantum" in QStyleFactory.keys():
                app.setStyle("kvantum")

    window = MainWindow()
    window.setWindowTitle("PyDeviceBackup")
    window.show()

    sys.exit(app.exec())
