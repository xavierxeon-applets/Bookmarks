#!/usr/bin/env python3

import sys

from lib import Console
from lib.fsync import ManagerAbstract


def printHelpAndExit():

   print(Console.cyan('fsync', light=False) + ' [command]')
   print('   sync folders')
   print('')
   print('   ' + Console.blue('COMMANDS:'))
   print('   * init [computer:path]: store the remote desination')
   print('   * pull: copy content from remote to local')
   print('   * push: copy content from local to remote')
   print('   * local: show local changes')
   print('   * remote: show remote changes')
   sys.exit(0)


def main():

   if len(sys.argv) < 3:
      printHelpAndExit()

   currentPath = sys.argv[1]
   command = sys.argv[2]
   tag = sys.argv[3] if len(sys.argv) >= 4 else None

   managerDict = dict()
   try:
      for manager in ManagerAbstract.__subclasses__():
         managerDict[manager.command()] = manager
   except NotImplementedError:
      print('>> exception in getting command <<')
      return

   if not command in managerDict:
      printHelpAndExit()

   manager = managerDict[command](currentPath, tag)
   try:
      manager.execute()
   except NotImplementedError:
      print('>> exception in executing command <<')
      return


if __name__ == '__main__':
   main()
