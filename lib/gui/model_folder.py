#

from .model_abstract import ModelAbstract

import os

from PySide6.QtGui import QStandardItem

from ..manager_abstract import ManagerAbstract


class ModelFolder(ModelAbstract):

   def __init__(self):

      ModelAbstract.__init__(self, ManagerAbstract.DirKey)
      self.update()

   def update(self):

      self.clear()
      self.setHorizontalHeaderLabels(['Name', 'Path'])

      data = self.loadData()
      for name, path in data.items():

         nameItem = QStandardItem(name)
         nameItem.setEditable(False)

         pathItem = QStandardItem(path)
         pathItem.setEditable(False)

         if not os.path.exists(path):
            nameItem.setForeground(ModelAbstract.ColorError)
            pathItem.setForeground(ModelAbstract.ColorError)

         self.invisibleRootItem().appendRow([nameItem, pathItem])
