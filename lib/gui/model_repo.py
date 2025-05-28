#

from .model_abstract import ModelAbstract

from PySide6.QtGui import QStandardItem

from ..manager_abstract import ManagerAbstract


class ModelRepo(ModelAbstract):

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.RepoKey)
      self.update()

   def update(self):

      self.clear()
      self.setHorizontalHeaderLabels(['Name', 'Url'])

      data = self.loadData()
      for name, url in data.items():

         nameItem = QStandardItem(name)
         nameItem.setEditable(False)

         urlItem = QStandardItem(url)
         urlItem.setEditable(False)

         self.invisibleRootItem().appendRow([nameItem, urlItem])
