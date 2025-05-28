#

from PySide6.QtWidgets import QTreeView

from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMenu


from ..manager_clear import ManagerClear


class TreeView(QTreeView):

   def __init__(self, manager, model):

      QTreeView.__init__(self)
      self._manager = manager
      self._model = model

      self.setModel(self._model)
      self.setRootIsDecorated(False)

      self.setContextMenuPolicy(Qt.CustomContextMenu)
      self.customContextMenuRequested.connect(self._contextMenuRequested)

      self._menuFunctions = {'Remove': self._remove}

   def prependContextMenuFunction(self, name, function):

      content = {name: function}
      self._menuFunctions = {**content, **self._menuFunctions}

   def _contextMenuRequested(self, position):

      index = self.indexAt(position)
      nameList = self._model.getNamesFromIndex(index)
      if not nameList:
         return

      menu = QMenu(self)
      for name, function in self._menuFunctions.items():
         if not function:
            menu.addSeparator()
         else:
            action = menu.addAction(name)
            nameFunction = partial(function, nameList)
            action.triggered.connect(nameFunction)

      pos = self.viewport().mapToGlobal(position)
      menu.exec_(pos)

   def _remove(self, nameList):

      if not nameList:
         return

      clearManager = ManagerClear(None, None)
      for name in nameList:
         clearManager.clear(self._model.sectionName, name)
      clearManager.save(False)

      self._model.update()
