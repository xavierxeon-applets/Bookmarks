#

import os

from .manager_abstract import ManagerAbstract

from ..console import Console


class ManagerInit(ManagerAbstract):

   @classmethod
   def command(cls):

      return 'init'

   def execute(self):

      self.save()
