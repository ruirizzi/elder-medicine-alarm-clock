# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ruiri\Desktop\alarm-clock\Tests\listtest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 



class Ui_MainWindow(object):
    inteiro = 0
    array = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 60, 75, 23))
        self.pushButton.clicked.connect(self.addItemToList)
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(360, 120, 75, 23))
        self.pushButton2.clicked.connect(self.removeItemToList)
        self.pushButton2.setObjectName("pushButton2")
        
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(360, 180, 75, 23))
        self.pushButton3.clicked.connect(self.clearItemToList)
        self.pushButton3.setObjectName("pushButton3")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.listaDoCaralho()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton2.setText(_translate("MainWindow", "Remove"))
        self.pushButton3.setText(_translate("MainWindow", "Clear"))

    def listaDoCaralho(self):
        self.listWidget.addItems(self.array)

    def addItemToList(self):
        self.inteiro += 1
        self.array.append(str(self.inteiro))
        self.listWidget.clear()
        self.listWidget.addItems(self.array)
    
    def removeItemToList(self):
        self.array.remove(self.array[-1])
        self.listWidget.clear()
        self.listWidget.addItems(self.array)

    def clearItemToList(self):
        self.array.clear()
        self.listWidget.clear()
        self.listWidget.addItems(self.array)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

