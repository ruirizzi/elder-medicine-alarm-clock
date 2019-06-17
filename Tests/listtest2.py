from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    inteiro = 0
    array = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 435)
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Adicionar\nHorario"))
        self.pushButton2.setText(_translate("MainWindow", "Remover\nHorario"))

    def addItemToList(self):
        indice = self.tableWidget.rowCount()
        horario = self.timeEdit.time()
        self.tableWidget.insertRow(indice)
        self.tableWidget.setItem(indice,0, QtWidgets.QTableWidgetItem(str(horario.hour()) + ":" + str(horario.minute())))
        self.tableWidget.setItem(indice,1, QtWidgets.QTableWidgetItem("Nome do remédio {}".format(indice)))

        self.listWidget.addItem(str(horario.hour()) + ":" + str(horario.minute()))

    def removeItemToList(self):
        itens = self.listWidget.selectedItems()
        for item in itens:
            self.listWidget.takeItem(self.listWidget.row(item))

        itens = self.tableWidget.selectedItems()
        for item in itens:
            indice = self.tableWidget.row(item)
            self.tableWidget.removeRow(indice)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

