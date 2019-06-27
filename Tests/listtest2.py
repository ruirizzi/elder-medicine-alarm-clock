from PyQt5 import QtCore, QtGui, QtWidgets
import threading, time, signal, datetime
from datetime import timedelta

WAIT_TIME_SECONDS = 5
scheduleList = list()

class ProgramKilled(Exception):
    pass


def check_for_pending_schedule():
    now = datetime.datetime.today()
    for s in scheduleList:
        if (s.dayOfWeek == now.weekday() or s.dayOfWeek == 7 ) and s.hour == now.hour and s.minute ==  now.minute:
            #TODO execute sound in another thread for X minutes
            print("New schedule found")
            if s.repeat is False:
                indice = scheduleList.index(s)
                scheduleList.remove(s)
                print(indice)
                ui.removeItemFromTableByIndex(indice) #apparently this works very well
    
def signal_handler(signum, frame):
    raise ProgramKilled

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 60, 75, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(360, 120, 75, 40))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
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
    
    def pushButtonClicked(self):
        #TODO Implement DOW selection
        #TODO Implement Description input
        now = self.timeEdit.time()
        schedule = classe.Schedule(now, "Descrição",  False, 7)
        scheduleList.append(schedule)
        self.addItemToTable(str(schedule.hour) + ':' + str(schedule.minute), schedule.description)

    def pushButton2Clicked(self):
        itens = self.tableWidget.selectedItems()
        for item in itens:
            index = self.tableWidget.row(item)
            self.removeItemFromTableByIndex(index)
            self.removeItemFromListByIndex(index)

    def removeItemFromListByIndex(self, index):
        scheduleList.remove(scheduleList[index])

    def removeItemFromTableByIndex(self, index):
        #TODO test with random-inserted schedules 
        self.tableWidget.removeRow(index) 

    def removeItemFromTableBySelection(self):
        itens = self.tableWidget.selectedItems()
        for item in itens:
            index = self.tableWidget.row(item)
            self.tableWidget.removeRow(index)
    
    def addItemToTable(self, cellValueFirstColumn, cellValueSecondColumn):
        index = self.tableWidget.rowCount()
        self.tableWidget.insertRow(index)
        self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(cellValueFirstColumn))
        self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(cellValueSecondColumn))

    
class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        
    def stop(self):
                self.stopped.set()
                self.join()
    def run(self):
            while not self.stopped.wait(self.interval.total_seconds()):
                self.execute(*self.args, **self.kwargs)

if __name__ == "__main__":
    import sys
    import classe
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=check_for_pending_schedule)
    job.start()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


while True:
    try:
        time.sleep(1)
    except ProgramKilled:
        print ("Program killed: running cleanup code")
        job.stop()
        break