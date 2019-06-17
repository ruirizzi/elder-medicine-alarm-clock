# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'C:\Users\ruiri\Desktop\alarm-clock\alarm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import events

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 331, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tabMain = QtWidgets.QWidget()
        self.tabMain.setObjectName("tabMain")
        self.lblSuperior = QtWidgets.QLabel(self.tabMain)
        self.lblSuperior.setGeometry(QtCore.QRect(10, 10, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.lblSuperior.setFont(font)
        self.lblSuperior.setTextFormat(QtCore.Qt.AutoText)
        self.lblSuperior.setObjectName("lblSuperior")
        self.lblInferior = QtWidgets.QLabel(self.tabMain)
        self.lblInferior.setGeometry(QtCore.QRect(10, 70, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.lblInferior.setFont(font)
        self.lblInferior.setTextFormat(QtCore.Qt.AutoText)
        self.lblInferior.setObjectName("lblInferior")
        self.btnSnooze = QtWidgets.QPushButton(self.tabMain)
        self.btnSnooze.setGeometry(QtCore.QRect(10, 130, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnSnooze.setFont(font)
        self.btnSnooze.setObjectName("btnSnooze")
        self.btnSnooze.clicked.connect(self.btnSnoozePressed)
        self.btnTaken = QtWidgets.QPushButton(self.tabMain)
        self.btnTaken.setGeometry(QtCore.QRect(150, 130, 161, 71))
        self.btnTaken.clicked.connect(self.btnTakenPressed)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btnTaken.setFont(font)
        self.btnTaken.setObjectName("btnTaken")
        self.tabWidget.addTab(self.tabMain, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.timeEditTime = QtWidgets.QTimeEdit(self.tabConfig)
        self.timeEditTime.setGeometry(QtCore.QRect(90, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.timeEditTime.setFont(font)
        self.timeEditTime.setObjectName("timeEditTime")
        self.lblTime = QtWidgets.QLabel(self.tabConfig)
        self.lblTime.setGeometry(QtCore.QRect(10, 10, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(7)
        self.lblTime.setFont(font)
        self.lblTime.setObjectName("lblTime")
        self.listWidget = QtWidgets.QListWidget(self.tabConfig)
        self.listWidget.setGeometry(QtCore.QRect(10, 130, 211, 81))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.tabConfig)
        self.lineEdit.setGeometry(QtCore.QRect(10, 59, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.btnNew = QtWidgets.QPushButton(self.tabConfig)
        self.btnNew.setGeometry(QtCore.QRect(230, 10, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNew.setFont(font)
        self.btnNew.setObjectName("btnNew")
        self.btnNew.clicked.connect(self.btnNewPressed)
        self.btnRemove = QtWidgets.QPushButton(self.tabConfig)
        self.btnRemove.setGeometry(QtCore.QRect(230, 130, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRemove.setFont(font)
        self.btnRemove.setObjectName("btnRemove")
        self.btnRemove.clicked.connect(self.btnRemovePressed)
        self.line = QtWidgets.QFrame(self.tabConfig)
        self.line.setGeometry(QtCore.QRect(10, 110, 301, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tabConfig, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblSuperior.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">SUP. 11CHAR</span></p></body></html>"))
        self.lblInferior.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">INF. 11CHAR</span></p></body></html>"))
        self.btnSnooze.setText(_translate("MainWindow", "Snooze"))
        self.btnTaken.setText(_translate("MainWindow", "TAKEN!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Main"))
        self.lblTime.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Schedule</span></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "MAX 11 CHAR"))
        self.btnNew.setText(_translate("MainWindow", "New \n"
"Schedule"))
        self.btnRemove.setText(_translate("MainWindow", "Remove \n"
"Selected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("MainWindow", "Config"))

    def btnSnoozePressed(self):
        events.printMessage("btnSnoozePressed")

    def btnTakenPressed(self):
        events.printMessage("btnTakenPressed")
    
    def btnNewPressed(self):
        events.printMessage("btnNewPressed")
    
    def btnRemovePressed(self):
        events.printMessage("btnRemovePressed")