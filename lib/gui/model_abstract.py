#

from PySide6.QtGui import QStandardItemModel

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

import json

from ..manager_abstract import ManagerAbstract


class ModelAbstract(QStandardItemModel):

   ColorError = QColor(Qt.red)

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
