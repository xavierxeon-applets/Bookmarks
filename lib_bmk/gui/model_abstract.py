#

from PySide6.QtGui import QStandardItemModel

import json

from .value_item import ValueItem

from ..manager_abstract import ManagerAbstract
from ..manager_clear import ManagerClear


class ModelAbstract(QStandardItemModel):

   def __init__(self, sectionName):

      QStandardItemModel.__init__(self)
      self.sectionName = sectionName

   def loadData(self):

      with open(ManagerAbstract._dbFileName, 'r') as infile:
         data = json.load(infile)

      return data[self.sectionName] if self.sectionName in data else dict()

   def getNamesFromIndex(self, indexList):

      if not indexList:
         return list()

      if not isinstance(indexList, list):
         indexList = [indexList]

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

   def roleNames(self):

      return ValueItem.roleNames()

   def doubleClicked(self, name):

      pass

   def removeSelected(self):

      nameList = self._getCheckedNames()
      if not nameList:
         return

      clearManager = ManagerClear(None, None)
      for name in nameList:
         clearManager.clear(self.sectionName, name)
      clearManager.save(False)

      self.update()

   def _getCheckedNames(self):

      nameList = list()
      for row in range(self.rowCount()):
         index = self.index(row, 0)
         item = self.itemFromIndex(index)
         if item.checked:
            nameList.append(item.name)

      return nameList
