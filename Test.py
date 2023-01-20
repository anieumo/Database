import sys
import os

from PyQt6.QtCore import Qt, QFileInfo, QUrl, qDebug, QEvent
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QAction, QMouseEvent
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QFileDialog, 
QListWidgetItem, QTreeView, QTreeWidget, QTreeWidgetItem, QMenu, QAbstractItemView)

class Copycat(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.browsebutton = QPushButton("Browse")
        self.browsebutton.clicked.connect(self.openBrowser)
        self.button = QPushButton("Add Sequence")
        self.button.clicked.connect(self.addSequence)
        self.addShotButton = QPushButton("Add Shot")
        self.addShotButton.clicked.connect(self.addShot)
        self.addSequenceLine = QLineEdit(self)
        self.addSequenceLine.returnPressed.connect(self.addSequenceItemOnReturn)
        self.addShotLine = QLineEdit(self)
        self.addShotLine.returnPressed.connect(self.addShotItemOnReturn)
        # shot item goes in as child of sequence

        self.treeView = QTreeWidget(self)
        self.treeView.setHeaderLabels(['Name', 'Date Modified', 'Size'])
        self.treeView.itemClicked.connect(self.detectClick)

        self.container = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.treeView)
        self.layout.addWidget(self.browsebutton)
        self.layout.addWidget(self.button)

        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def openBrowser(self):
        dialog = QFileDialog(self)
        dialog.show()
        fileName = dialog.getOpenFileName()
        

        fileurl = dialog.getOpenFileUrl()
        print(fileurl[0])
        url = QUrl(fileurl[0])
        qurl = QUrl.toLocalFile(url)
        print(qurl)
        basename = os.path.basename(qurl)
        print(basename)
        self.treeView.addItem(basename)

    def addSequence(self):
        self.addSequenceLine.clear()
        self.layout.addWidget(self.addSequenceLine)
        self.addSequenceLine.show()
        # self.input = self.add.text()
        self.item = QTreeWidgetItem(self.treeView)
        self.layout.addWidget(self.addShotButton)


    def detectClick(self, event):
        print("detect click")

    def addSequenceItemOnReturn(self):
        self.addSequenceLine.hide()
        sequenceName = self.addSequenceLine.text()
        if sequenceName != "":
            self.item.setText(0, sequenceName)
            print(self.item.text(0))

    def addShot(self):
        if not self.item.isSelected():
            print("please add a sequence or select a sequence, first")
            return
        else:
            self.layout.addWidget(self.addShotLine)
            childItem = QTreeWidgetItem()
            # childItem.setText(0, "test")
            # self.item.addChild(childItem)

    def addShotItemOnReturn(self):
        childItem = QTreeWidgetItem()
        shotname = self.addShotLine.text()
        childItem.setText(0, shotname)
        self.item.addChild(childItem)
        self.addShotLine.hide()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        removeAction = QAction("Remove", self)
        # removeAction.triggered.connect()
        contextMenu.addAction(removeAction)

        openOnDiskAction = QAction("Open on Disk", self)
        # openOnDiskAction.triggered.connect()
        contextMenu.addAction(openOnDiskAction)

        copyDiskPathAction = QAction("Copy Disk Path")
        # copyDiskPathAction.triggered.connect()
        contextMenu.addAction(copyDiskPathAction)

        updateAction = QAction("Update")
        # updateAction.triggered.connect(updateAction)
        contextMenu.addAction(updateAction)

        quitAction = QAction("Quit", self)
        contextMenu.addAction(quitAction)
        action = contextMenu.exec(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.close()
        self.treeView.itemClicked()

app = QApplication(sys.argv)

window = Copycat()
window.show()

app.exec()