#

from .model_abstract import ModelAbstract

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem

from ..manager_abstract import ManagerAbstract


class ItemRepo(QStandardItem):

   def __init__(self, name, url):

      QStandardItem.__init__(self)

      self.name = name
      self.url = url

      self.setEditable(False)

   def data(self, role):

      if role == ModelAbstract.RoleName:
         return self.name
      elif role == ModelRepo.RoleUrl:
         return self.url

      return QStandardItem.data(self, role)


class ModelRepo(ModelAbstract):

   RoleUrl = Qt.UserRole + 2

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.RepoKey)
      self.update()

   def update(self):

      self.clear()

      data = self.loadData()
      for name, url in data.items():
         item = ItemRepo(name, url)
         self.invisibleRootItem().appendRow([item])

   def roleNames(self):

      data = dict()
      data[ModelAbstract.RoleName] = 'name'.encode()
      data[ModelRepo.RoleUrl] = 'url'.encode()

      return data
