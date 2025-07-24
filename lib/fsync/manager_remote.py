#
import sys

from .manager_abstract import ManagerAbstract
from .console import Console


class ManagerRemote(ManagerAbstract):

   def __init__(self, currentPath, tag):

      ManagerAbstract.__init__(self, currentPath, tag)

   @classmethod
   def command(cls):

      return 'remote'

   def execute(self):

      remote = self._getRemote()
      print(Console.green('REMOTE STATUS') + ' of ' + Console.yellow(remote))
      self._listDiff(remote, self.currentPath)
