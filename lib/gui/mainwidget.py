#
from PySide6.QtWidgets import QWidget

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QVBoxLayout, QLabel, QTreeView, QPushButton

from .model_folder import ModelFolder
from .model_repo import ModelRepo
from .settings import Settings
from ..console import Console


class MainWidget(QWidget):

   def __init__(self, manager):

      super().__init__()
      self.setWindowTitle('Bookmarks Manager')

      self.modelFolder = ModelFolder(manager)
      self.modelRepo = ModelRepo(manager)

      self.labelFolder = QLabel('Folders')

      self.treeViewFolder = QTreeView()
      self.treeViewFolder.setRootIsDecorated(False)
      self.treeViewFolder.setModel(self.modelFolder)

      self.deleteFolderButton = QPushButton('Delete Folder')
      self.deleteFolderButton.clicked.connect(self.removeFolder)

      self.labelRepo = QLabel('Repositories')

      self.treeViewRepo = QTreeView()
      self.treeViewRepo.setRootIsDecorated(False)
      self.treeViewRepo.setModel(self.modelRepo)

      self.deleteRepoButton = QPushButton('Delete Repository')
      self.deleteRepoButton.clicked.connect(self.removeRepo)

      self.masterLayout = QVBoxLayout()
      self.setLayout(self.masterLayout)

      self.masterLayout.addWidget(self.labelFolder)
      self.masterLayout.addWidget(self.treeViewFolder)
      self.masterLayout.addWidget(self.deleteFolderButton)

      self.masterLayout.addWidget(self.labelRepo)
      self.masterLayout.addWidget(self.treeViewRepo)
      self.masterLayout.addWidget(self.deleteRepoButton)

      settings = Settings()
      self.restoreGeometry(settings.value('geometry', b''))

      print('settings @ ', settings.fileName())

   def closeEvent(self, event):

      settings = Settings()
      settings.setValue('geometry', self.saveGeometry())

      event.accept()

   def removeFolder(self):

      self.modelFolder.removeSelection(self.treeViewFolder)

   def removeRepo(self):

      self.modelRepo.removeSelection(self.treeViewRepo)
