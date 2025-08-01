#!/usr/bin/env python3

import sys

from lib import Console
from lib.bmk import ManagerAbstract


def printHelpAndExit():

   print(Console.cyan('bmk', light=False) + ' [command] [tag]')
   print('   jump around the file system')
   print('')
   print('   ' + Console.blue('COMMANDS FOLDERS:'))
   print('   * store [tag]: store the current dir')
   print('   * jump [tag]: jump to tagged dir')
   print('   * jump: show jump selection')
   print('')
   print('   ' + Console.blue('COMMANDS REPOS:'))
   print('   * store_repo [tag]: store the current git repo')
   print('   * reclone [tag]: clone repo in current dir')
   print('   * reclone: show reclone selection')
   print('')
   print('   ' + Console.blue('COMMANDS SYNC:'))
   print('   * store_sync [tag]: store the current folder sync')
   print('   * resync [tag]: folder sync in current dir')
   print('   * resync: show folder sync selection')
   print('')
   print('   ' + Console.blue('COMMANDS ADMIN:'))
   print('   * list: list stored dirs and repos')
   print('   * clear [tag]: remove tag')
   print('   * gui: show the admin gui')
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
