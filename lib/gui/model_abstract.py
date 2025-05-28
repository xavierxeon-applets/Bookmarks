#

from PySide6.QtGui import QStandardItemModel

import json

from ..manager_abstract import ManagerAbstract
from ..console import Console


class ModelAbstract(QStandardItemModel):

   def __init__(self, manager, sectionName):

      QStandardItemModel.__init__(self)
      self._manager = manager
      self._sectionName = sectionName

   def loadData(self):

      with open(ManagerAbstract._dbFileName, 'r') as infile:
         data = json.load(infile)

      return data[self._sectionName] if self._sectionName in data else dict()

   def removeSelection(self, treeView):

      if not treeView:
         return

      nameList = self._getNamesFromSelection(treeView)
      if not nameList:
         return

      for name in nameList:

         print(Console.green('removed tag'), ':', name)
         del self._manager.data[self._sectionName][name]

      self._manager.save(False)
      self.update()

   def _getNamesFromSelection(self, treeView):

      indexList = treeView.selectedIndexes()
      if not indexList:
         return list()

      rowList = list()
      for index in indexList:
         if not index.isValid():
            continue

         row = index.row()
         if row not in rowList:
            rowList.append(row)

      nameList = list()
      for row in rowList:
         index = self.index(row, 0)
         nameItem = self.itemFromIndex(index)
         name = nameItem.text()
         nameList.append(name)

      return nameList
