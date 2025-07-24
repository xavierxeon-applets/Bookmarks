#

import os
import sys
from pathlib import Path

from .console import Console

from .manager_abstract import ManagerAbstract


class ManagerReclone(ManagerAbstract):

   _repoFile = str(Path.home()) + '/.bookmarks/repo'
   _RecloneExitCode = 44

   @classmethod
   def command(cls):

      return 'reclone'

   def execute(self):

      if not self.tag:
         self.cloneSelection()
         return

      self._cloneInternal(self.tag)

   def cloneSelection(self):

      index = 1
      tagDict = dict()
      for tag, giturl in self.data[ManagerAbstract.RepoKey].items():
         tagDict[index] = (tag, giturl)
         index = index + 1

      if not tagDict:
         print(Console.blue('no bookmarks available'))
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
      self._cloneInternal(gotoTag)

   def _cloneInternal(self, gotoTag):

      if not gotoTag in self.data[ManagerAbstract.RepoKey]:
         print(Console.magenta('tag not stored'), ':', gotoTag)
         return

      giturl = self.data[ManagerAbstract.RepoKey][gotoTag]

      with open(ManagerReclone._repoFile, 'w') as outfile:
         outfile.write(giturl)

      sys.exit(ManagerReclone._RecloneExitCode)
