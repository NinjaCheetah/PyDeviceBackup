# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 505)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(4)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.device_name_lbl = QLabel(self.centralwidget)
        self.device_name_lbl.setObjectName(u"device_name_lbl")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.device_name_lbl.setFont(font1)

        self.verticalLayout_3.addWidget(self.device_name_lbl)

        self.device_type_lbl = QLabel(self.centralwidget)
        self.device_type_lbl.setObjectName(u"device_type_lbl")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.device_type_lbl.setFont(font2)

        self.verticalLayout_3.addWidget(self.device_type_lbl)

        self.ios_version_lbl = QLabel(self.centralwidget)
        self.ios_version_lbl.setObjectName(u"ios_version_lbl")

        self.verticalLayout_3.addWidget(self.ios_version_lbl)

        self.device_udid_lbl = QLabel(self.centralwidget)
        self.device_udid_lbl.setObjectName(u"device_udid_lbl")

        self.verticalLayout_3.addWidget(self.device_udid_lbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_3.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_3)

        self.start_backup_btn = QPushButton(self.centralwidget)
        self.start_backup_btn.setObjectName(u"start_backup_btn")

        self.verticalLayout_6.addWidget(self.start_backup_btn)

        self.start_restore_btn = QPushButton(self.centralwidget)
        self.start_restore_btn.setObjectName(u"start_restore_btn")

        self.verticalLayout_6.addWidget(self.start_restore_btn)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backup_dir_entry = QLineEdit(self.centralwidget)
        self.backup_dir_entry.setObjectName(u"backup_dir_entry")

        self.horizontalLayout_2.addWidget(self.backup_dir_entry)

        self.choose_backup_dir_btn = QPushButton(self.centralwidget)
        self.choose_backup_dir_btn.setObjectName(u"choose_backup_dir_btn")

        self.horizontalLayout_2.addWidget(self.choose_backup_dir_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_4)

        self.backup_key_entry = QLineEdit(self.centralwidget)
        self.backup_key_entry.setObjectName(u"backup_key_entry")
        self.backup_key_entry.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.backup_key_entry)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.status_lbl = QLabel(self.centralwidget)
        self.status_lbl.setObjectName(u"status_lbl")

        self.verticalLayout_2.addWidget(self.status_lbl)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.verticalLayout_2.addWidget(self.progress_bar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 29))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PyDeviceBackup", None))
        self.device_name_lbl.setText(QCoreApplication.translate("MainWindow", u"No Device Connected", None))
        self.device_type_lbl.setText(QCoreApplication.translate("MainWindow", u"Connect a device to begin", None))
        self.ios_version_lbl.setText(QCoreApplication.translate("MainWindow", u"iOS Version:", None))
        self.device_udid_lbl.setText(QCoreApplication.translate("MainWindow", u"UDID: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Backup Options", None))
        self.start_backup_btn.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.start_restore_btn.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Backup Folder:", None))
        self.choose_backup_dir_btn.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Encryption Key:", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"Ready.", None))
    # retranslateUi

