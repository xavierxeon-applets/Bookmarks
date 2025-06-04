#

from .model_abstract import ModelAbstract, Item

from ..manager_abstract import ManagerAbstract


class ModelRepo(ModelAbstract):

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.RepoKey)
      self.update()

   def update(self):

      self.clear()

      data = self.loadData()
      for name, url in data.items():
         item = Item(name, url)
         self.invisibleRootItem().appendRow([item])
