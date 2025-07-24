#

import sys

from .manager_abstract import ManagerAbstract
from .console import Console


class ManagerPush(ManagerAbstract):

   def __init__(self, currentPath, tag):

      ManagerAbstract.__init__(self, currentPath, tag)

   @classmethod
   def command(cls):

      return 'push'

   def execute(self):

      remote = self._getRemote()
      print(Console.green('PUSH') + ' to ' + Console.yellow(remote))
      self._sync(self.currentPath, remote)
