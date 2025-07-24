#
import sys

from .manager_abstract import ManagerAbstract
from ..console import Console


class ManagerLocal(ManagerAbstract):

   def __init__(self, currentPath, tag):

      ManagerAbstract.__init__(self, currentPath, tag)

   @classmethod
   def command(cls):

      return 'local'

   def execute(self):

      remote = self._getRemote()
      print(Console.green('LOCAL STATUS'))
      self._listDiff(self.currentPath, remote)
