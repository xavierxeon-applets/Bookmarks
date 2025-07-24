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
         if not self.tag in self.data[sectionName]:
            continue

         del self.data[sectionName][self.tag]
         found = True
         print(Console.green('removed tag'), ':', self.tag, ' from section', sectionName)

      if not found:
         print(Console.magenta('unkown tag'), ':', self.tag)
         return

      self.save()
