#
from PySide6.QtGui import QStandardItem

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class ValueItem(QStandardItem):

   RoleName = Qt.UserRole + 1
   RoleValue = Qt.UserRole + 2
   RoleBackgroundColor = Qt.UserRole + 3
   RoleTextColor = Qt.UserRole + 4
   RoleInteraction = Qt.UserRole + 5

   def __init__(self, name, value, exists=True):

      QStandardItem.__init__(self)

      self.name = name
      self.value = value
      self.exists = exists

      self.checked = False

      self.setEditable(False)

   def data(self, role):

      if role == ValueItem.RoleName:
         return self.name
      elif role == ValueItem.RoleValue:
         return self.value
      elif role == ValueItem.RoleBackgroundColor:
         if self.checked:
            return QColor(Qt.gray)
         else:
            return QColor(Qt.white)
      elif role == ValueItem.RoleTextColor:
         if self.exists:
            return QColor(Qt.black)
         else:
            return QColor(Qt.red)

      return QStandardItem.data(self, role)

   def setData(self, value, role):

      if ValueItem.RoleInteraction == role:
         if 'clicked' in value:
            self.checked = not self.checked
         elif 'doubleClicked' in value:
            self.checked = not self.checked
            print(f'double clicked {self.name} ')
         else:
            print(f'intraction {value} @ {self.name}')

   @staticmethod
   def roleNames():

      data = dict()
      data[ValueItem.RoleName] = b'name'
      data[ValueItem.RoleValue] = b'value'
      data[ValueItem.RoleBackgroundColor] = b'bgcolor'
      data[ValueItem.RoleTextColor] = b'textcolor'
      data[ValueItem.RoleInteraction] = b'interaction'

      return data
