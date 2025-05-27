#

import os
from subprocess import run

from .manager_abstract import ManagerAbstract
from .console import Console


class ManagerRepo(ManagerAbstract):

   @classmethod
   def command(cls):

      return 'repo'

   def execute(self):

      if not self.tag:
         print(Console.magenta('not tag given'))
         return

      result = run(['git', 'config', '--get', 'remote.origin.url'], capture_output=True)
      giturl = result.stdout
      if not giturl:
         print(Console.red('not a git repository'))
         return

      giturl = giturl.decode().strip()
      self.data[ManagerAbstract.RepoKey][self.tag] = giturl
      print('stored ' + Console.yellow(self.tag) + ' @ ' + giturl)
      self.save()
