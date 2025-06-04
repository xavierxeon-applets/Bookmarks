#

from .model_abstract import ModelAbstract, Item


from ..manager_abstract import ManagerAbstract


class ModelFolder(ModelAbstract):

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.DirKey)
      self.update()

   def update(self):

      self.clear()

      data = self.loadData()
      for name, path in data.items():
         item = Item(name, path)
         self.invisibleRootItem().appendRow([item])
