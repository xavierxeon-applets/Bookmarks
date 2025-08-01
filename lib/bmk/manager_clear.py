#

from .manager_abstract import ManagerAbstract

from ..console import Console


class ManagerClear(ManagerAbstract):

   @classmethod
   def command(cls):

      return 'clear'

   def execute(self):

      if not self.tag:
         print(Console.magenta('no tag given'))
         return

      found = False
      for sectionName in [ManagerAbstract.DirKey, ManagerAbstract.RepoKey, ManagerAbstract.SyncKey]:

         if self.clear(sectionName, self.tag):
            found = True

      if not found:
         print(Console.magenta('unkown tag'), ':', self.tag)
         return

      self.save()

   def clear(self, sectionName, name):

      if not name in self.data[sectionName]:
         return False

      del self.data[sectionName][name]
      print(Console.green('removed tag'), ':', name, ' from section', sectionName)
      return True
