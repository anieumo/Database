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
            return QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/book.png")
        elif fileInfo.fileName() in tier2:
            return QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/color-palette.png")
        elif fileInfo.fileName() in tier3:
            return QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/paper-plane.png")
        elif fileInfo.fileName() in tier4:
            return QIcon("/Users/aniediumoren/Desktop/CopycatDatabase/camera.png")
        return QFileIconProvider.icon(self, fileInfo)

class Main(QTreeView):
    def __init__(self):
        QTreeView.__init__(self)
        """setting up the QSystem Model"""
        self.setWindowTitle("Shot Database")
        self.label = QLabel("Test")
        self.input = QLineEdit()
        self.model = QFileSystemModel()
        self.setModel(self.model)
        self.model.setRootPath(QDir.rootPath())
        self.setRootIndex(self.model.index("/Users/aniediumoren/Desktop/asset"))

        self.model.setIconProvider(IconProvider())
        self.resize(800, 600)

    def contextMenuEvent(self, event):
        """Setting up right click context Menu"""
        contextMenu = QMenu(self)

        ### sets up context menu options
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

        action = contextMenu.exec(self.mapToGlobal(event.pos()))

    def openOnDisk(self):
        """Context Menu: Open on Disk feature"""
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        print(filePath)
        ### open
        subprocess.call(['open', filePath])

    def copyFilePath(self):
        """Context Menu: Copy File Path"""
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        print(filePath)
        ### copy
        subprocess.run("pbcopy", text=True, input=filePath)

    def createAsset(self):
        """Context Menu: Create Asset Feature"""
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
        """Context Menu: Create New Version"""
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
        """Context Menu: Create New Shot"""
        indexs = self.selectedIndexes()
        for i in indexs:
            filePath = self.model.filePath(i)
        try:
            global destinationfilename
            destinationfilename = filePath
            print(destinationfilename)
            if not os.path.exists(destinationfilename):
                return
            else:
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
        """Context Menu: Create New Sequence feature"""
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
    """Context Menu: Create New Sequence feature"""
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Create Asset")
        self.instructionLabel = QLabel("Search for Asset:")
        self.selectAsssetTypeLabel = QLabel("Select Asset Type:")
        self.input = QLineEdit()

        self.filelocation = None
  
        self.input = QLineEdit()
        self.input.setText(self.filelocation)

        self.combobox = QComboBox()
        self.combobox.addItems(tier2)

        self.createAssetButton = QPushButton("Browse")
        self.createAssetButton.clicked.connect(self.createAsset)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.selectAsssetTypeLabel)
        self.layout.addWidget(self.combobox)
        self.layout.addWidget(self.createAssetButton)
        self.layout.addWidget(self.instructionLabel)
        self.layout.addWidget(self.input)

        self.setLayout(self.layout)
        self.resize(200, 400)

    def createAsset(self):
        self.dialog = QFileDialog()
        file = self.dialog.getOpenFileName()
        self.filelocation = file[0]
        print(self.filelocation)
        self.input.setText(self.filelocation)

        pathhead = os.path.basename(self.filelocation)
        print(pathhead)
        asset = os.path.splitext(pathhead)[0]
        print(asset)
        assetType = self.combobox.currentText()
        # add validation so incorrect assttype cannot be selected
        destinationPath = os.path.join(destinationfilename, assetType, "version1")
        os.makedirs(destinationPath)
        print(destinationPath)
        print(self.filelocation)
        shutil.copy(self.filelocation, destinationPath)
        self.close()

class CreateVersionPopup(QWidget):
    """Popup window that handles creating a new version"""
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Create New Version")

        self.dialog = QFileDialog()

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
        """Calculates version number for labeling"""
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

        print(testagain)
        num = "1234567890"
        print(num)
        string2 = []
        versionnum = []
        for i in latest:
            if i not in num:
                string2.append(i)
            else:
                versionnum.append(i)
        print(versionnum)
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
    """Popup window for creating a new shot"""
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Create New Shot")
        self.label = QLabel("Name Shot:")
        self.input = QLineEdit()
        self.errorlabel = QLabel()

        self.createShotButton = QPushButton("Create Shot")
        self.createShotButton.clicked.connect(self.createShot)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.createShotButton)
        self.layout.addWidget(self.errorlabel)

        self.setLayout(self.layout)
        self.resize(200, 400)
    
    def createShot(self):
        """Creates shot path"""
        text = self.input.text()
        # if NameError:
        #     self.errorlabel.setText("Please close window, select a sequence and try again")
        #     return
        print(destinationfilename)
        newShotPath = os.path.join(destinationfilename, text)
        os.makedirs(newShotPath)
        self.close()

class CreateNewSequencePopup(QWidget):
    """Popup window to create new sequnce"""
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
        pathName = "/Users/aniediumoren/Desktop/asset"
        newSequencePath = os.path.join(pathName, text)
        os.makedirs(newSequencePath)
   
if __name__ == '__main__':
    ### allows us to execute code as a script instead of a module
    ### store code only ran when file is executed as a script
    import sys
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    app.exec()
    sys.exit()
