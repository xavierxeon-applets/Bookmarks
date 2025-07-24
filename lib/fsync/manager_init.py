#

import sys

from .manager_abstract import ManagerAbstract
from .console import Console


class ManagerInit(ManagerAbstract):

   def __init__(self, currentPath, tag):

      ManagerAbstract.__init__(self, currentPath, tag)

   @classmethod
   def command(cls):

      return 'init'

   def execute(self):

      if not self.tag:
         print(Console.magenta('no ssh source given'))
         return

      print(Console.green('REMOTE ') + self.tag)

      with open('.fsync', 'w') as outfile:
         outfile.write(self.tag)
