import sys
import os
from os.path import expanduser
# import pyperclip

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class TreeView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # home = expanduser('~')
        path = "open /Users/aniediumoren/Documents/asset"
        
        self.treeView = QTreeView(self)
        self.model = QFileSystemModel(self)
        self.model.setRootPath(QDir.rootPath())
        self.treeView.setRootIndex(self.model.index("/Users/aniediumoren/Desktop/asset"))
        self.treeView.setModel(self.model)

        # self.treeView.setRootPath(self.model.index(path))

        self.container = QWidget()

        # self.filterproxy = QSortFilterProxyModel()
        # self.filterproxy.setSourceModel(self.model)
        # self.filterproxy.setFilterKeyColumn(0)

        self.treeView.setModel(self.model)


        self.search = QLineEdit()
        self.search.textChanged.connect(self.function)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.treeView)

        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def function(self):
        search = []
        search.append(self.search.text())
        # if self.search.text() in self.model.fileName():
        self.treeView.keyboardSearch()
        # self.treeView.setModel(null)

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        removeAction = QAction("Remove", self)
        # removeAction.triggered.connect()
        contextMenu.addAction(removeAction)

        openOnDiskAction = QAction("Open on Disk", self)
        openOnDiskAction.triggered.connect(self.openOnDisk)
        contextMenu.addAction(openOnDiskAction)

        copyDiskPathAction = QAction("Copy Disk Path")
        copyDiskPathAction.triggered.connect(self.copyFilePath)
        contextMenu.addAction(copyDiskPathAction)

        updateAction = QAction("Update")
        # updateAction.triggered.connect(updateAction)
        contextMenu.addAction(updateAction)

        quitAction = QAction("Quit", self)
        contextMenu.addAction(quitAction)
        action = contextMenu.exec(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.close()

    def openOnDisk(self):
        indexs = self.treeView.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        print(filePath)
        os.open(filePath)

    def copyFilePath(self):
        indexs = self.treeView.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        print(filePath)





if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')
    main = TreeView()
    main.show()
    app.exec()
    sys.exit()
