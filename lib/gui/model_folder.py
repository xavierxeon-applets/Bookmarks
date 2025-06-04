#

from .model_abstract import ModelAbstract

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem

from ..manager_abstract import ManagerAbstract


class ItemFolder(QStandardItem):

   def __init__(self, name, path):

      QStandardItem.__init__(self)

      self.name = name
      self.path = path

      self.setEditable(False)

   def data(self, role):

      if role == ModelAbstract.RoleName:
         return self.name
      elif role == ModelFolder.RolePath:
         return self.path

      return QStandardItem.data(self, role)


class ModelFolder(ModelAbstract):

   RolePath = Qt.UserRole + 2

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.DirKey)
      self.update()

   def update(self):

      self.clear()

      data = self.loadData()
      for name, path in data.items():
         item = ItemFolder(name, path)
         self.invisibleRootItem().appendRow([item])

   def roleNames(self):

      data = dict()
      data[ModelAbstract.RoleName] = 'name'.encode()
      data[ModelFolder.RolePath] = 'path'.encode()

      return data
