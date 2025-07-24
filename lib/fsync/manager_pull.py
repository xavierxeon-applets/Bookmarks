#!/usr/bin/env python3

import sys

from .manager_abstract import ManagerAbstract
from ..console import Console


class ManagerPull(ManagerAbstract):

   def __init__(self, currentPath, tag):

      ManagerAbstract.__init__(self, currentPath, tag)

   @classmethod
   def command(cls):

      return 'pull'

   def execute(self):

      remote = self._getRemote()
      print(Console.green('PULL') + ' from ' + Console.yellow(remote))
      self._sync(remote, self.currentPath)
