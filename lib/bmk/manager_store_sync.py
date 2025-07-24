#

import os
from subprocess import run

from .manager_abstract import ManagerAbstract
from ..console import Console


class ManagerStoreSync(ManagerAbstract):

   @classmethod
   def command(cls):

      return 'store_sync'

   def execute(self):

      if not self.tag:
         print(Console.magenta('not tag given'))
         return

      syncTarget = self._getSyncTarget()
      if not syncTarget:
         print(Console.red('not a fsync folder'))
         return

      self.data[ManagerAbstract.SyncKey][self.tag] = syncTarget
      print('stored ' + Console.yellow(self.tag) + ' @ ' + syncTarget)
      self.save()

   def _getSyncTarget(self):

      syncFile = self.currentPath + '/.fsync'
      if not os.path.exists(syncFile):
         return None

      with open(syncFile, 'r') as f:
         return f.read().strip()

      return None
