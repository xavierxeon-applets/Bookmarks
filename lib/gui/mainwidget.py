#
from PySide6.QtWidgets import QWidget

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QVBoxLayout, QLabel, QTreeView, QPushButton

from .model_folder import ModelFolder
from .model_repo import ModelRepo


class MainWidget(QWidget):

   def __init__(self):

      super().__init__()
      self.setWindowTitle('Bookmarks Manager')

      self.modelFolder = ModelFolder()
      self.modelRepo = ModelRepo()

      self.labelFolder = QLabel('Folders')
      self.treeViewFolder = QTreeView()
      self.treeViewFolder.setModel(self.modelFolder)
      self.deleteFolderButton = QPushButton('Delete Folder')

      self.labelRepo = QLabel('Repositories')
      self.treeViewRepo = QTreeView()
      self.treeViewRepo.setModel(self.modelRepo)
      self.deleteRepoButton = QPushButton('Delete Repository')

      self.masterLayout = QVBoxLayout()
      self.setLayout(self.masterLayout)

      self.masterLayout.addWidget(self.labelFolder)
      self.masterLayout.addWidget(self.treeViewFolder)
      self.masterLayout.addWidget(self.deleteFolderButton)

      self.masterLayout.addWidget(self.labelRepo)
      self.masterLayout.addWidget(self.treeViewRepo)
      self.masterLayout.addWidget(self.deleteRepoButton)

      settings = QSettings()
      self.restoreGeometry(settings.value('geometry', b''))

      print('settings @ ', settings.fileName())

   def closeEvent(self, event):

      settings = QSettings()
      settings.setValue('geometry', self.saveGeometry())

      event.accept()
