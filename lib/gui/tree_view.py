#

from PySide6.QtWidgets import QTreeView

import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMenu

from ..console import Console
from ..manager_abstract import ManagerAbstract
from ..manager_jump import ManagerJump


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
      path = self._manager.data[ManagerAbstract.DirKey][name]

      if not os.path.exists(path):
         print(Console.red('direcotry does not exists'), ':', path, 'for tag', name)
         return

      with open(ManagerJump._jumpFile, 'w') as outfile:
         outfile.write(path)

      sys.exit(ManagerJump._JumpExitCode)

   def _remove(self, nameList):

      for name in nameList:

         print(Console.green('removed tag'), ':', name)
         del self._manager.data[self._model.sectionName][name]

      self._manager.save(False)
      self._model.update()
