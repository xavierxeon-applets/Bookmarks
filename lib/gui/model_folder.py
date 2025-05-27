#

from PySide6.QtGui import QStandardItemModel


class ModelFolder(QStandardItemModel):

   def __init__(self):

      super().__init__()

      self.setHorizontalHeaderLabels(['Name', 'Type', 'Size', 'Date'])
      self.setColumnCount(4)
      self.setRowCount(0)
