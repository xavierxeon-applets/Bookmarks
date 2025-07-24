#

import sys
import os
from subprocess import run
from pathlib import Path
from unittest import result

from .console import Console


class ManagerAbstract:

   _rsyncFile = str(Path.home()) + '/.foldersync'
   _RsyncExitCode = 33

   def __init__(self, currentPath, tag):

      self.currentPath = currentPath
      self.tag = tag

      self.standardParams = ['--archive',
                             '--compress',
                             '--human-readable',
                             '--partial',
                             '--delete',
                             '--progress',
                             '--exclude',
                             f'{self.currentPath}/.fsync']

   @classmethod
   def command(cls):

      raise NotImplementedError

   def execute(self):

      raise NotImplementedError

   def _getRemote(self):

      def abort():
         print(Console.red('No remote set'))
         sys.exit(1)

      try:
         with open('.fsync', 'r') as infile:
            remote = infile.readline().strip()
      except FileNotFoundError:
         abort()

      if not remote:
         abort()

      return remote

   def _sync(self, source, target):

      with open(ManagerAbstract._rsyncFile, 'w') as outfile:
         params = ' '.join(self.standardParams)
         command = f'rsync {params}  {source}/* {target}'
         outfile.write(command)

      sys.exit(ManagerAbstract._RsyncExitCode)

   def _listDiff(self, source, target):

      with open(ManagerAbstract._rsyncFile, 'w') as outfile:
         params = ' '.join(self.standardParams)
         command = f'rsync --dry-run {params} {source}/* {target}'
         outfile.write(command)

      command = ['bash', ManagerAbstract._rsyncFile]
      result = run(command, shell=False, capture_output=True)
      os.remove(ManagerAbstract._rsyncFile)

      content = result.stdout.decode('utf-8')
      content = content.strip()
      if not content:
         print(Console.blue('No differences found'))
         return

      content = content.split('\n')
      for entry in content:
         entry = entry.strip()
         if not entry:
            continue

         print(f' * {entry}')
