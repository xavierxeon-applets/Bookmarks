#

from PySide6.QtGui import QStandardItemModel

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QColor

import json

from ..manager_abstract import ManagerAbstract


class Item(QStandardItem):

   def __init__(self, name, url):

      QStandardItem.__init__(self)

      self.name = name
      self.url = url

      self.setEditable(False)

   def data(self, role):

      if role == ModelAbstract.RoleName:
         return self.name
      elif role == ModelAbstract.RoleValue:
         return self.url

      return QStandardItem.data(self, role)

   def setData(self, value, role):

      if ModelAbstract.RoleMouse == role:
         print(f'mouse @ {value}')


class ModelAbstract(QStandardItemModel):

   ColorError = QColor(Qt.red)
   RoleName = Qt.UserRole + 1
   RoleValue = Qt.UserRole + 2
   RoleMouse = Qt.UserRole + 3

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

      data = dict()
      data[ModelAbstract.RoleName] = 'name'.encode()
      data[ModelAbstract.RoleValue] = 'value'.encode()
      data[ModelAbstract.RoleMouse] = 'mouse'.encode()

      return data
