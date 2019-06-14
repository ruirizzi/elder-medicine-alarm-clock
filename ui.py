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
        self.btnSileciar = QtWidgets.QPushButton(self.tabMain)
        self.btnSileciar.setGeometry(QtCore.QRect(10, 130, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnSileciar.setFont(font)
        self.btnSileciar.setObjectName("btnSileciar")
        self.btnSileciar.clicked.connect(self.btnSilenciarPressed)
        self.btnTomei = QtWidgets.QPushButton(self.tabMain)
        self.btnTomei.setGeometry(QtCore.QRect(150, 130, 161, 71))
        self.btnTomei.clicked.connect(self.btnTomeiPressed)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btnTomei.setFont(font)
        self.btnTomei.setObjectName("btnTomei")
        self.tabWidget.addTab(self.tabMain, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.timeEditHorario = QtWidgets.QTimeEdit(self.tabConfig)
        self.timeEditHorario.setGeometry(QtCore.QRect(90, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.timeEditHorario.setFont(font)
        self.timeEditHorario.setObjectName("timeEditHorario")
        self.lblHora = QtWidgets.QLabel(self.tabConfig)
        self.lblHora.setGeometry(QtCore.QRect(10, 10, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(7)
        self.lblHora.setFont(font)
        self.lblHora.setObjectName("lblHora")
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
        self.btnNova = QtWidgets.QPushButton(self.tabConfig)
        self.btnNova.setGeometry(QtCore.QRect(230, 10, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNova.setFont(font)
        self.btnNova.setObjectName("btnNova")
        self.btnNova.clicked.connect(self.btnNovaPressed)
        self.btnRemover = QtWidgets.QPushButton(self.tabConfig)
        self.btnRemover.setGeometry(QtCore.QRect(230, 130, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRemover.setFont(font)
        self.btnRemover.setObjectName("btnRemover")
        self.btnRemover.clicked.connect(self.btnRemoverPressed)
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
        self.btnSileciar.setText(_translate("MainWindow", "Silenciar"))
        self.btnTomei.setText(_translate("MainWindow", "Tomei!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Principal"))
        self.lblHora.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Horário</span></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "MÁX 11 CHAR"))
        self.btnNova.setText(_translate("MainWindow", "Novo \n"
"Remédio"))
        self.btnRemover.setText(_translate("MainWindow", "Remover \n"
"Selecionado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("MainWindow", "Configurações"))

    def btnSilenciarPressed(self):
        events.printarMensagem("btnSilenciarPressed")

    def btnTomeiPressed(self):
        events.printarMensagem("btnTomeiPressed")
    
    def btnNovaPressed(self):
        events.printarMensagem("btnNovaPressed")
    
    def btnRemoverPressed(self):
        events.printarMensagem("btnRemoverPressed")