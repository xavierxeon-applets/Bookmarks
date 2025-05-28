#
from PySide6.QtWidgets import QWidget


from PySide6.QtWidgets import QVBoxLayout, QLabel

from .model_folder import ModelFolder
from .model_repo import ModelRepo
from .settings import Settings
from .tree_view import TreeView
from ..manager_jump import ManagerJump


class MainWidget(QWidget):

   def __init__(self, manager):

      super().__init__()
      self.setWindowTitle('Bookmarks Manager')

      self.modelFolder = ModelFolder()
      self.modelRepo = ModelRepo()

      self.labelFolder = QLabel('Folders')

      self.treeViewFolder = TreeView(manager, self.modelFolder)
      self.treeViewFolder.prependContextMenuFunction('Jump', self._jump)
      self.treeViewFolder.prependContextMenuFunction('Spacer', None)

      self.labelRepo = QLabel('Repositories')

      self.treeViewRepo = TreeView(manager, self.modelRepo)

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

   def _jump(self, nameList):

      if not nameList:
         return

      name = nameList[0]
      jumpManager = ManagerJump(None, name)
      return jumpManager.execute()
