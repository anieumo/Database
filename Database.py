import sys
import os
import subprocess
import shutil

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

_PATHNAME = None

tier1 = ["version1", "version2", "version3", "version4", "version5", "version6", "version7"]
tier2 = ["mesh.main", "mesh.maps", "previz", "anim.cache"]
tier3 = ["1010", "1020", "1030", "1040", "1050", "2010", "3010"]
tier4 = ["ace", "ads"]

class IconProvider(QFileIconProvider):
    def icon(self, fileInfo):
        if fileInfo.fileName() in tier1:
            return QIcon("/Users/aniediumoren/Desktop/CopycatTessa/book.png")
        elif fileInfo.fileName() in tier2:
            return QIcon("/Users/aniediumoren/Desktop/CopycatTessa/color-palette.png")
        elif fileInfo.fileName() in tier3:
            return QIcon("/Users/aniediumoren/Desktop/CopycatTessa/paper-plane.png")
        elif fileInfo.fileName() in tier4:
            return QIcon("/Users/aniediumoren/Desktop/CopycatTessa/camera.png")
        return QFileIconProvider.icon(self, fileInfo)

class Main(QTreeView):
    def __init__(self):
        QTreeView.__init__(self)
        self.setWindowTitle("Shot Database")
        self.label = QLabel("Test")
        self.input = QLineEdit()
        self.model = QFileSystemModel()
        self.setModel(self.model)
        self.addlayout(self.label)
        self.model.setRootPath(QDir.rootPath())
        self.setRootIndex(self.model.index("/Users/aniediumoren/Desktop/asset"))
        # self.clicked.connect(self.add)

        self.model.setIconProvider(IconProvider())
        self.resize(800, 600)

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)

        openOnDiskAction = QAction("Open on Disk", self)
        openOnDiskAction.setIcon(QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/Folder.png"))
        openOnDiskAction.triggered.connect(self.openOnDisk)
        contextMenu.addAction(openOnDiskAction)

        copyDiskPathAction = QAction("Copy Disk Path")
        copyDiskPathAction.setIcon(QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/CopyFolder.png"))
        copyDiskPathAction.triggered.connect(self.copyFilePath)
        contextMenu.addAction(copyDiskPathAction)

        creatAssetAction = QAction("Create Asset")
        creatAssetAction.setIcon(QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/color-palette.png"))
        creatAssetAction.triggered.connect(self.createAsset)
        contextMenu.addAction(creatAssetAction)

        createElementAction = QAction("Create New Version")
        createElementAction.setIcon(QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/book.png"))
        createElementAction.triggered.connect(self.createNewVersion)
        contextMenu.addAction(createElementAction)

        createNewShotAction = QAction("Create New Shot")
        createNewShotAction.setIcon(QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/paper-plane.png"))
        createNewShotAction.triggered.connect(self.createNewShot)
        contextMenu.addAction(createNewShotAction)

        createNewSequenceAction = QAction("Create New Sequence")
        createNewSequenceAction.setIcon(QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/cassette.png"))
        createNewSequenceAction.triggered.connect(self.createNewSequence)
        contextMenu.addAction(createNewSequenceAction)

        # quitAction = QAction("Quit", self)
        # quitAction.setIcon(QIcon("/Users/aniediumoren/Desktop/CopycatTessa/remove.png"))
        # contextMenu.addAction(quitAction)
        action = contextMenu.exec(self.mapToGlobal(event.pos()))
        # if action == quitAction:
        #     self.close()

    def openOnDisk(self):
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        print(filePath)
        subprocess.call(['open', filePath])

    def copyFilePath(self):
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        print(filePath)
        subprocess.run("pbcopy", text=True, input=filePath)

    # def add(self):
    #     index = self.currentIndex()
    #     print(index)
    #     path = self.model.filePath(index)
    #     print(self.model.filePath(index))
    #     print(self.model.fileName(index))
    #     print(self.model.index(path, column = 0))

    def createAsset(self):
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        print(filePath)
        subprocess.call(['open', filePath])

        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        _PATHNAME = filePath
        global destinationfilename
        destinationfilename = filePath
        print(_PATHNAME)

        print("Opening a new popup window...")
        self.w = CreateAssetPopup()
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.show()
    
    def createNewVersion(self):
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        _PATHNAME = filePath
        global destinationfilename
        destinationfilename = filePath
        print(_PATHNAME)

        print("Opening a new popup window...")
        self.x = CreateVersionPopup()
        self.x.setGeometry(QRect(100, 100, 400, 200))
        self.x.show()

    def createNewShot(self):
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        try:
            global destinationfilename
            destinationfilename = filePath
            print("Opening a new popup window...")
            self.y = CreateNewShotPopup()
            self.y.setGeometry(QRect(100, 100, 400, 200))
            self.y.show()

        except:
            print("Opening a new popup window...")
            self.y = CreateNewShotPopup()
            self.y.setGeometry(QRect(100, 100, 400, 200))
            self.y.show()

    def createNewSequence(self):
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        try:
            global destinationfilename
            destinationfilename = filePath
            print("Opening a new popup window...")
            self.z = CreateNewSequencePopup()
            self.z.setGeometry(QRect(100, 100, 400, 200))
            self.z.show()
        except:
            print("Opening a new popup window...")
            self.z = CreateNewSequencePopup()
            self.z.setGeometry(QRect(100, 100, 400, 200))
            self.z.show()
    

class CreateAssetPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Create Asset")
        self.instructionLabel = QLabel("Search for Asset:")
        # self.instructionLabel.setAlignment(AlignCenter)
        self.selectAsssetTypeLabel = QLabel("Select Asset Type:")
        self.input = QLineEdit()
        self.dialog = QFileDialog()

        file = self.dialog.getOpenFileName()
        print(file)
        self.filelocation = file[0]
        print(self.filelocation)

        self.input = QLineEdit()
        self.input.setText(self.filelocation)

        self.combobox = QComboBox()
        self.combobox.addItems(tier2)

        self.createAssetButton = QPushButton("Create")
        self.createAssetButton.clicked.connect(self.createAsset)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.instructionLabel)
        self.layout.addWidget(self.input)

        self.layout.addWidget(self.selectAsssetTypeLabel)
        self.layout.addWidget(self.combobox)
        self.layout.addWidget(self.createAssetButton)

        self.setLayout(self.layout)
        self.resize(200, 400)

    def createAsset(self):
        pathhead = os.path.basename(self.filelocation)
        print(pathhead)
        print(destinationfilename)
        asset = os.path.splitext(pathhead)[0]
        print(asset)
        assetType = self.combobox.currentText()
        # add validation so incorrect assttype cannot be selected
        destinationPath = os.path.join(destinationfilename, asset, assetType, "version1",pathhead)
        print(destinationPath)
        print(self.filelocation)
        # shutil.copy(self.filelocation, destinationPath)

class CreateVersionPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Create New Version")

        self.dialog = QFileDialog()

        # self.dialog.title("search for asset")

        self.file = self.dialog.getOpenFileName()
        print(self.file)
        self.filelocation = self.file[0]
        print(self.filelocation)

        self.createVersionButton = QPushButton("Create New Version")
        self.createVersionButton.clicked.connect(self.createVersion)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.createVersionButton)

        self.setLayout(self.layout)
        self.resize(200, 400)

    def createVersion(self):
        ### grab latest version in directory:
        destinationFileNameHead = os.path.split(destinationfilename)[0]
        listVersionsInDirectory = os.listdir(destinationFileNameHead)
        listVersionsInDirectory.sort()
        print(listVersionsInDirectory)
        latestVersion = listVersionsInDirectory[-1]
        pathOfLatestVersion = os.path.join(destinationFileNameHead, latestVersion)
        print(pathOfLatestVersion)

        # create new version name
        latest = os.path.basename(pathOfLatestVersion)
        testagain = os.path.split(pathOfLatestVersion)[0]
        # print(test)
        num = "1234567890"
        print(num)
        string2 = []
        versionnum = []
        for i in latest:
            if i not in num:
                string2.append(i)
            else:
                versionnum.append(i)
        versionnumber = ''.join(versionnum)
        print(versionnumber)
        versionnumber = int(versionnumber) + 1
        string2 = ''.join(string2)
        newstring = string2 + str(versionnumber)
        ### check that version grabbed is latest
        print(newstring)
        newVersionNumber = os.path.basename(pathOfLatestVersion).replace(latest, newstring)
        print(newVersionNumber)

        #create name of new file
        pathName = os.path.split(destinationfilename)[0]
        print(self.filelocation)
        basename = os.path.split(self.filelocation)[1]
        print(basename)
        newDir = os.path.join(pathName, newVersionNumber)
        newPathName = os.path.join(pathName, newVersionNumber, basename)

        #mkdir of new file and copy
        print(newPathName)
        os.makedirs(newDir)
        shutil.copy(self.filelocation, newPathName)
        self.close()

class CreateNewShotPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Create New Shot")
        self.label = QLabel("Name Shot:")
        self.input = QLineEdit()

        self.createShotButton = QPushButton("Create Shot")
        self.createShotButton.clicked.connect(self.createShot)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.createShotButton)

        self.setLayout(self.layout)
        self.resize(200, 400)
    
    def createShot(self):
        text = self.input.text()
        print(destinationfilename)
        newShotPath = os.path.join(destinationfilename, text)
        os.makedirs(newShotPath)
        self.close()

class CreateNewSequencePopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Create Sequence")
        self.label = QLabel("Name Sequence:")
        self.input = QLineEdit()

        self.createSequenceButton = QPushButton("Create Sequence")
        self.createSequenceButton.clicked.connect(self.createSequence)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.createSequenceButton)

        self.setLayout(self.layout)
        self.resize(200, 400)

    def createSequence(self):
        text = self.input.text()
        tier4.append(text)
        print(tier4)
        pathName = "/Users/aniediumoren/Desktop/asset"
        newSequencePath = os.path.join(pathName, text)
        os.makedirs(newSequencePath)

            
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    app.exec()
    sys.exit()
