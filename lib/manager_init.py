#!/usr/bin/env python3

import os

from .manager_abstract import ManagerAbstract

from xxpystuff.tools import Console

class ManagerInit(ManagerAbstract):

   def __init__(self, currentPath, tag):

      ManagerAbstract.__init__(self, currentPath, tag)

   @classmethod
   def command(cls):

      return 'init'    
      
   def execute(self):

      self.save()      
               