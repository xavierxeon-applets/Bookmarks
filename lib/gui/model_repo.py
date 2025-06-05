#

from .model_abstract import ModelAbstract
from .value_item import ValueItem

from ..manager_abstract import ManagerAbstract


class ModelRepo(ModelAbstract):

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.RepoKey)
      self.update()

   def update(self):

      self.clear()

      data = self.loadData()
      for name, url in data.items():
         item = ValueItem(name, url)
         self.invisibleRootItem().appendRow([item])
