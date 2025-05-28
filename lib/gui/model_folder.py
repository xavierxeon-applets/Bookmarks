#

from .model_abstract import ModelAbstract

from PySide6.QtGui import QStandardItem

from ..manager_abstract import ManagerAbstract


class ModelFolder(ModelAbstract):

   def __init__(self, manager):

      ModelAbstract.__init__(self, manager, ManagerAbstract.DirKey)
      self.update()

   def update(self):

      self.clear()
      self.setHorizontalHeaderLabels(['Name', 'Path'])

      data = self.loadData()
      for name, path in data.items():
         nameItem = QStandardItem(name)
         pathItem = QStandardItem(path)
         self.invisibleRootItem().appendRow([nameItem, pathItem])
