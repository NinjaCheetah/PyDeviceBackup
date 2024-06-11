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
        MainWindow.resize(533, 676)
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

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.backup_dir_entry = QLineEdit(self.centralwidget)
        self.backup_dir_entry.setObjectName(u"backup_dir_entry")

        self.horizontalLayout.addWidget(self.backup_dir_entry)

        self.choose_backup_dir_btn = QPushButton(self.centralwidget)
        self.choose_backup_dir_btn.setObjectName(u"choose_backup_dir_btn")

        self.horizontalLayout.addWidget(self.choose_backup_dir_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_backup_btn = QPushButton(self.centralwidget)
        self.start_backup_btn.setObjectName(u"start_backup_btn")

        self.horizontalLayout_2.addWidget(self.start_backup_btn)

        self.start_restore_btn = QPushButton(self.centralwidget)
        self.start_restore_btn.setObjectName(u"start_restore_btn")

        self.horizontalLayout_2.addWidget(self.start_restore_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.backup_key_entry = QLineEdit(self.centralwidget)
        self.backup_key_entry.setObjectName(u"backup_key_entry")
        self.backup_key_entry.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.backup_key_entry)

        self.status_lbl = QLabel(self.centralwidget)
        self.status_lbl.setObjectName(u"status_lbl")

        self.verticalLayout_2.addWidget(self.status_lbl)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.verticalLayout_2.addWidget(self.progress_bar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 533, 30))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PyDeviceBackup", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Backup Folder:", None))
        self.choose_backup_dir_btn.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Controls:", None))
        self.start_backup_btn.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.start_restore_btn.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Encryption Key:", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"Ready.", None))
    # retranslateUi

