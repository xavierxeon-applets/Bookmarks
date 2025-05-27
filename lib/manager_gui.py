#

import os

from .manager_abstract import ManagerAbstract


class ManagerGui(ManagerAbstract):

   def __init__(self, currentPath, tag):

      ManagerAbstract.__init__(self, currentPath, tag)

   @classmethod
   def command(cls):

      return 'gui'

   def execute(self):

      from .gui import main_gui
      main_gui()
