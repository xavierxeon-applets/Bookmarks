#

from .manager_abstract import ManagerAbstract

from .console import Console


class ManagerClear(ManagerAbstract):

   @classmethod
   def command(cls):

      return 'clear'

   def execute(self):

      if not self.tag:
         print(Console.magenta('no tag given'))
         return

      inDir = self.tag in self.data[ManagerAbstract.DirKey]
      inRepo = self.tag in self.data[ManagerAbstract.RepoKey]
      if not inDir and not inRepo:
         print(Console.magenta('unkown tag'), ':', self.tag)
         return

      if inDir:
         del self.data[ManagerAbstract.DirKey][self.tag]
      if inRepo:
         del self.data[ManagerAbstract.RepoKey][self.tag]

      self.save()

      print(Console.green('removed tag'), ':', self.tag)
