import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeView
# from PyQt6.Qt import QStandardItemModel, QStandardItem
from PyQt6.QtGui import QFont, QColor, QStandardItemModel


class CopycatDatabase(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("CopyCat")
        self.browsebutton = QWidget.QPushButton()
        self.browsebutton.clicked.connect(self._openBrowser)

        self.treeView = QTreeView(self)
        
        layout = QVBoxLayout(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Date Modified', 'Size'])
        self.tree.header().setDefaultSectionSize(180)
        self.tree.setModel(self.model)
        self.importData(data)
        self.tree.expandAll()


app = QApplication(sys.argv)

window = CopycatDatabase()
window.show()

app.exec()
