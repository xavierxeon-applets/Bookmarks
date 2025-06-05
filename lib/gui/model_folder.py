#


from .model_abstract import ModelAbstract

import os
from functools import partial

from PySide6.QtCore import QTimer

from .value_item import ValueItem

from ..manager_abstract import ManagerAbstract
from ..manager_jump import ManagerJump


class ModelFolder(ModelAbstract):

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.DirKey)
      self.update()

   def update(self):

      self.clear()

      data = self.loadData()
      for name, path in data.items():
         exists = os.path.exists(path)
         item = ValueItem(name, path, exists)
         self.invisibleRootItem().appendRow([item])

   def doubleClicked(self, name):

      my_function = partial(self._jump, name)
      QTimer.singleShot(0, my_function)

   def _jump(self, name):

      jumpManager = ManagerJump(None, name)
      return jumpManager.execute()
