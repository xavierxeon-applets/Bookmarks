#
from PySide6.QtWidgets import QWidget


from PySide6.QtWidgets import QVBoxLayout, QLabel, QStatusBar

from .model_folder import ModelFolder
from .model_repo import ModelRepo
from .settings import Settings
from .tree_view import TreeView
from ..manager_jump import ManagerJump


class MainWidget(QWidget):

   def __init__(self, manager):

      super().__init__()
      self.setWindowTitle('Bookmarks Manager')

      # folder
      self.modelFolder = ModelFolder()
      self.labelFolder = QLabel('Folders')

      self.treeViewFolder = TreeView(manager, self.modelFolder)
      self.treeViewFolder.prependContextMenuFunction('Jump', self._jump)
      self.treeViewFolder.prependContextMenuFunction('Spacer', None)

      # repository
      self.modelRepo = ModelRepo()
      self.labelRepo = QLabel('Repositories')

      self.treeViewRepo = TreeView(manager, self.modelRepo)

      # other
      self.statusBar = QStatusBar()

      # layout
      self.masterLayout = QVBoxLayout()
      self.setLayout(self.masterLayout)

      self.masterLayout.addWidget(self.labelFolder)
      self.masterLayout.addWidget(self.treeViewFolder)

      self.masterLayout.addWidget(self.labelRepo)
      self.masterLayout.addWidget(self.treeViewRepo)

      self.masterLayout.addWidget(self.statusBar)

      # settings
      settings = Settings()
      print('settings @ ', settings.fileName())

      self.restoreGeometry(settings.value('geometry', b''))

   def closeEvent(self, event):

      settings = Settings()
      settings.setValue('geometry', self.saveGeometry())

      event.accept()

   def _jump(self, nameList):

      if not nameList:
         return

      name = nameList[0]
      jumpManager = ManagerJump(None, name)
      return jumpManager.execute()
