#

from .model_abstract import ModelAbstract

from PySide6.QtGui import QStandardItem

from ..manager_abstract import ManagerAbstract


class ModelRepo(ModelAbstract):

   def __init__(self, manager):

      ModelAbstract.__init__(self, manager, ManagerAbstract.RepoKey)
      self.update()

   def update(self):

      self.clear()
      self.setHorizontalHeaderLabels(['Name', 'Url'])

      data = self.loadData()
      for name, url in data.items():
         nameItem = QStandardItem(name)
         urlItem = QStandardItem(url)
         self.invisibleRootItem().appendRow([nameItem, urlItem])
