# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\UP\interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\UP\\../Downloads/free-icon-stairway-4568057.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #3c3c3c;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.icon_label = QtWidgets.QLabel(self.centralwidget)
        self.icon_label.setGeometry(QtCore.QRect(610, 70, 200, 200))
        self.icon_label.setText("")
        self.icon_label.setPixmap(QtGui.QPixmap("D:\\UP\\../Downloads/icon_app (1).png"))
        self.icon_label.setObjectName("icon_label")
        self.button_start_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_pause.setGeometry(QtCore.QRect(640, 460, 100, 100))
        self.button_start_pause.setStyleSheet("background-color: none;\n"
"border: 0px;")
        self.button_start_pause.setObjectName("button_start_pause")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(500, 425, 421, 22))
        self.horizontalSlider.setStyleSheet("QSlider{\n"
"  background: #3c3c3c;\n"
"}\n"
"QSlider::groove:horizontal {  \n"
"  height: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"    background: #B0AEB1;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"  background: #8d0000;\n"
"    border: 1px solid #8d0000;\n"
"    width: 17px;\n"
"    margin: -5px 0; \n"
"    border-radius: 8px;\n"
"}\n"
"QSlider::sub-page:qlineargradient {\n"
"  background: #671e1e;\n"
"     border-radius: 5px;\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.button_next = QtWidgets.QPushButton(self.centralwidget)
        self.button_next.setGeometry(QtCore.QRect(770, 460, 100, 100))
        self.button_next.setStyleSheet("background-color: none;\n"
"border: 0px;")
        self.button_next.setObjectName("button_next")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(510, 460, 100, 100))
        self.button_back.setStyleSheet("background-color: none;\n"
"border: 0px;")
        self.button_back.setObjectName("button_back")
        self.button_loop = QtWidgets.QPushButton(self.centralwidget)
        self.button_loop.setEnabled(True)
        self.button_loop.setGeometry(QtCore.QRect(890, 490, 35, 35))
        self.button_loop.setStyleSheet("background-color: #8d0000;")
        self.button_loop.setObjectName("button_loop")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 310, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(470, 10, 3, 580))
        self.line.setStyleSheet("background-color: #8d0000;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 581))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    background-color: #8d0000;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #a91613;\n"
"}\n"
"")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listView_base = QtWidgets.QListView(self.tab)
        self.listView_base.setGeometry(QtCore.QRect(5, 1, 441, 551))
        self.listView_base.setStyleSheet("border: 0px;")
        self.listView_base.setObjectName("listView_base")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listView_user = QtWidgets.QListView(self.tab_2)
        self.listView_user.setGeometry(QtCore.QRect(5, 1, 441, 551))
        self.listView_user.setStyleSheet("border: 0px;\n"
"")
        self.listView_user.setObjectName("listView_user")
        self.tabWidget.addTab(self.tab_2, "")
        self.button_download = QtWidgets.QPushButton(self.centralwidget)
        self.button_download.setGeometry(QtCore.QRect(510, 20, 50, 50))
        self.button_download.setStyleSheet("background: 0px;\n"
"border: 0px;")
        self.button_download.setObjectName("button_download")
        self.label_now = QtWidgets.QLabel(self.centralwidget)
        self.label_now.setGeometry(QtCore.QRect(500, 400, 55, 16))
        self.label_now.setText("")
        self.label_now.setAlignment(QtCore.Qt.AlignCenter)
        self.label_now.setObjectName("label_now")
        self.label_all = QtWidgets.QLabel(self.centralwidget)
        self.label_all.setGeometry(QtCore.QRect(860, 400, 55, 16))
        self.label_all.setText("")
        self.label_all.setAlignment(QtCore.Qt.AlignCenter)
        self.label_all.setObjectName("label_all")
        MainWindow.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_loop, self.button_next)
        MainWindow.setTabOrder(self.button_next, self.button_start_pause)
        MainWindow.setTabOrder(self.button_start_pause, self.button_back)
        MainWindow.setTabOrder(self.button_back, self.horizontalSlider)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CellarMusic"))
        self.button_start_pause.setText(_translate("MainWindow", "PushButton"))
        self.button_next.setText(_translate("MainWindow", "PushButton"))
        self.button_back.setText(_translate("MainWindow", "PushButton"))
        self.button_loop.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Текущая песня"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Плейлист приложения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Пользовательский плейлист"))
        self.button_download.setText(_translate("MainWindow", "PushButton"))
        self.action.setText(_translate("MainWindow", "Открыть"))
