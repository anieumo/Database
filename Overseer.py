import sys
import os
import csv

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


# everyday needs its own csv file to write and update to
# and to call data from on open

_SAVEPATH = None
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        self.calendar = QCalendarWidget(self)
        self.calendar.selectionChanged.connect(self.createDate)
        today = self.calendar.selectedDate()
        self.calendar.setMaximumDate(today)

        date = self.calendar.selectedDate()
        date = QDate.getDate(date)
        date = str(date)
        date = date.replace(", ", ".")
        date = date[1:11]
        self.date = "Timecard." + date + ".csv"
        print(self.date)
        self.savepath = "/Users/aniediumoren/Desktop/Overseer/"
        self.path = os.path.join(self.savepath, self.date)

        self.table = QTableWidget()
        self.table.setRowCount(1)
        self.table.setColumnCount(5)
        i = 0
        for i in range(5):
            self.table.setItem(0,i, QTableWidgetItem("0"))

        self.table.setHorizontalHeaderLabels(['Task', 'Logged Days', 'Hours', 'Week Total', 'Note'])
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.show()
        
        self.setText = QPushButton('Load CSV Data In')
        self.setText.clicked.connect(self.loadcsvdata)
        self.exportbutton = QPushButton('Export to Excel')
        self.exportbutton.clicked.connect(self.exportAsCSV)

        self.container = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.exportbutton)
        self.layout.addWidget(self.setText)

        
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def loadcsvdata(self, test):
        test = _SAVEPATH
        with open(test, 'r') as csvfile:
            reader = csv.reader(csvfile, dialect='excel', lineterminator='\n')
            for row in reader:
                end = int(row)
                print(int(row))
                for item in row[1:end]:
                    print(item)
                    num = 0
                    while num < 5:
                        self.table.setItem(0,num, QTableWidgetItem(item))
                        num = num + 1

    def resavepath(self):
        date = self.calendar.selectedDate()
        qdate = QDate.getDate(date)
        stringQDate = str(qdate)
        setDateFormat = stringQDate.replace(", ", ".")
        setDateString = setDateFormat[1:11]
        filename = "Timecard." + setDateString + ".csv"
        savePathHead = "/Users/aniediumoren/Desktop/Overseer/"
        savePath = os.path.join(savePathHead, filename)
        _SAVEPATH = savePath

    def createDate(self):
        self.exportAsCSV()

        # grabs savepath
        if self.calendar.selectedDate():
            date = self.calendar.selectedDate()
            qdate = QDate.getDate(date)
            stringQDate = str(qdate)
            setDateFormat = stringQDate.replace(", ", ".")
            setDateString = setDateFormat[1:11]
            filename = "Timecard." + setDateString + ".csv"
            savePathHead = "/Users/aniediumoren/Desktop/Overseer/"
            savePath = os.path.join(savePathHead, filename)
            _SAVEPATH = savePath
            print(_SAVEPATH)

        # imports any saved data
            test = _SAVEPATH
            if not _SAVEPATH:
                return
            with open(test, 'r') as csvfile:
                reader = csv.reader(csvfile, dialect='excel', lineterminator='\n')
                itemlist = []
                for row in reader:
                    for item in row:
                        print(item)
                        itemlist.append(item)
                print(itemlist)
                sansheader = int(len(itemlist)/2)
                print(sansheader)
                data = itemlist[sansheader::1]
                itemsToList = []
                itemsToList.append(data)
                print(itemsToList)
                i = 0
                for i in range(sansheader):
                    self.table.setItem(0,i, QTableWidgetItem(item))

            #set header
            self.table.setHorizontalHeaderLabels(['Task', 'Logged Days', 'Hours', 'Week Total', 'Note'])

    def exportAsCSV(self):
        # broken doesnt catch selectedDay
        # catch cancel case
        # needs mnual self.resavepath

        self.path, ok = QFileDialog.getSaveFileName(
            self, 'Save CSV', self.path, 'CSV(*.csv)')
        if ok:
            columns = range(self.table.columnCount())
            header = [self.table.horizontalHeaderItem(column).text()
                    for column in columns]
            with open(self.path, 'w') as csvfile:
                writer = csv.writer(
                    csvfile, dialect='excel', lineterminator='\n')
                writer.writerow(header)
                for row in range(self.table.rowCount()):
                    writer.writerow(
                        self.table.item(row, column).text()
                        for column in columns)

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__=='__main__':
    run()
