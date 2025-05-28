#

import sys
import os
import json
from pathlib import Path


class ManagerAbstract:

   _dbFileName = str(Path.home()) + '/.bookmarks/config.json'
   _completeFileName = str(Path.home()) + '/.bookmarks/complete.sh'
   _CompleteExitCode = 22
   DirKey = 'directories'
   RepoKey = 'repositories'

   def __init__(self, currentPath, tag):

      self.currentPath = currentPath
      self.tag = tag

      self.data = dict()
      if os.path.exists(ManagerAbstract._dbFileName):
         try:
            with open(ManagerAbstract._dbFileName, 'r') as infile:
               self.data = json.load(infile)
         except json.JSONDecodeError:
            print(f'Error: Failed to read JSON file {ManagerAbstract._dbFileName}. Please check the file format.')

      if not ManagerAbstract.DirKey in self.data:
         self.data[ManagerAbstract.DirKey] = dict()
      if not ManagerAbstract.RepoKey in self.data:
         self.data[ManagerAbstract.RepoKey] = dict()

   @classmethod
   def command(cls):

      raise NotImplementedError

   def execute(self):

      raise NotImplementedError

   def save(self, exit=True):

      with open(ManagerAbstract._dbFileName, 'w') as outfile:
         json.dump(self.data, outfile, indent=3)

      jumpKeys = self.data[ManagerAbstract.DirKey].keys()
      recloneKeys = self.data[ManagerAbstract.RepoKey].keys()
      with open(ManagerAbstract._completeFileName, 'w') as outfile:
         outfile.write('complete -W "' + ' '.join(list(jumpKeys)) + '" jump\n')
         outfile.write('complete -W "' + ' '.join(list(recloneKeys)) + '" reclone\n')

      if exit:
         sys.exit(ManagerAbstract._CompleteExitCode)
