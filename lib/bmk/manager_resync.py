#

import os
import sys
from pathlib import Path

from ..console import Console

from .manager_abstract import ManagerAbstract


class ManagerResync(ManagerAbstract):

   _syncFile = str(Path.home()) + '/.bookmarks/sync'
   _SyncExitCode = 55

   @classmethod
   def command(cls):

      return 'resync'

   def execute(self):

      if not self.tag:
         self.syncSelection()
         return

      self._syncInternal(self.tag)

   def syncSelection(self):

      index = 1
      tagDict = dict()
      for tag, giturl in self.data[ManagerAbstract.SyncKey].items():
         tagDict[index] = (tag, giturl)
         index = index + 1

      if not tagDict:
         print(Console.blue('no sync folders available'))
         return

      for index, data in tagDict.items():
         print(Console.yellow(str(index)), ':', data[0], Console.grey(data[1]))

      selection = input(Console.green('select number '))
      try:
         index = int(selection)
      except ValueError:
         index = None

      if not index in tagDict:
         print(Console.magenta('invalid selection'))
         return

      gotoTag = tagDict[index][0]
      self._syncInternal(gotoTag)

   def _syncInternal(self, gotoTag):

      if not gotoTag in self.data[ManagerAbstract.SyncKey]:
         print(Console.magenta('tag not stored'), ':', gotoTag)
         return

      syncTarget = self.data[ManagerAbstract.SyncKey][gotoTag]
      with open(ManagerResync._syncFile, 'w') as outfile:
         outfile.write(syncTarget)

      sys.exit(ManagerResync._SyncExitCode)
