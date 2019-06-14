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
        MainWindow.resize(522, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 60, 75, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addItemToList)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(360, 120, 75, 40))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.removeItemToList)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAlternatingRowColors(True)
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(360, 180, 75, 40))
        self.timeEdit.setObjectName("timeEdit")
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



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Adicionar\nHorario"))
        self.pushButton2.setText(_translate("MainWindow", "Remover\nHorario"))

    def addItemToList(self):
        horario = self.timeEdit.time()
        self.listWidget.addItem(str(horario.hour()) + ":" + str(horario.minute()))

    def removeItemToList(self):
        itens = self.listWidget.selectedItems()

        for item in itens:
            self.listWidget.takeItem(self.listWidget.row(item))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

