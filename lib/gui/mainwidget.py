#
from PySide6.QtWidgets import QWidget


from PySide6.QtWidgets import QVBoxLayout, QLabel

from .model_folder import ModelFolder
from .model_repo import ModelRepo
from .settings import Settings
from .tree_view import TreeView


class MainWidget(QWidget):

   def __init__(self, manager):

      super().__init__()
      self.setWindowTitle('Bookmarks Manager')

      self.modelFolder = ModelFolder()
      self.modelRepo = ModelRepo()

      self.labelFolder = QLabel('Folders')

      self.treeViewFolder = TreeView(manager, self.modelFolder, True)

      self.labelRepo = QLabel('Repositories')

      self.treeViewRepo = TreeView(manager, self.modelRepo, False)

      self.masterLayout = QVBoxLayout()
      self.setLayout(self.masterLayout)

      self.masterLayout.addWidget(self.labelFolder)
      self.masterLayout.addWidget(self.treeViewFolder)

      self.masterLayout.addWidget(self.labelRepo)
      self.masterLayout.addWidget(self.treeViewRepo)

      settings = Settings()
      self.restoreGeometry(settings.value('geometry', b''))

      print('settings @ ', settings.fileName())

   def closeEvent(self, event):

      settings = Settings()
      settings.setValue('geometry', self.saveGeometry())

      event.accept()
