#

import os

from .manager_abstract import ManagerAbstract

from .console import Console


class ManagerStore(ManagerAbstract):

   @classmethod
   def command(cls):

      return 'store'

   def execute(self):

      if not self.tag:
         print(Console.magenta('not tag given'))
         return

      self.data[ManagerAbstract.DirKey][self.tag] = self.currentPath
      print('stored ' + Console.yellow(self.tag) + ' @ ' + self.currentPath)
      self.save()
