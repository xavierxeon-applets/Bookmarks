#

from PySide6.QtWidgets import QTreeView


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMenu

from ..console import Console
from ..manager_jump import ManagerJump
from ..manager_clear import ManagerClear


class TreeView(QTreeView):

   def __init__(self, manager, model, hasJump):

      QTreeView.__init__(self)
      self._manager = manager
      self._model = model
      self._hasJump = hasJump

      self.setModel(self._model)
      self.setRootIsDecorated(False)

      self.setContextMenuPolicy(Qt.CustomContextMenu)
      self.customContextMenuRequested.connect(self._contextMenuRequested)

   def _contextMenuRequested(self, position):

      index = self.indexAt(position)
      nameList = self._model.getNamesFromIndex(index)
      if not nameList:
         return

      menu = QMenu(self)
      if self._hasJump:
         jump_action = menu.addAction("Jump")
         menu.addSeparator()
      remove_action = menu.addAction("Remove")

      pos = self.viewport().mapToGlobal(position)
      selected_action = menu.exec_(pos)

      if selected_action == remove_action:
         self._remove(nameList)
      elif self._hasJump and selected_action == jump_action:
         self._jump(nameList)

   def _jump(self, nameList):

      if not nameList:
         return

      name = nameList[0]
      jumpManager = ManagerJump(None, name)
      return jumpManager.execute()

   def _remove(self, nameList):

      if not nameList:
         return

      clearManager = ManagerClear(None, None)
      for name in nameList:
         clearManager.clear(self._model.sectionName, name)
      clearManager.save(False)

      self._model.update()
