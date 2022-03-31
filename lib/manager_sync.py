#!/usr/bin/env python3

import os

from .manager_abstract import ManagerAbstract

from .console import Console
from .process import Process


class ManagerSync(ManagerAbstract):

    def __init__(self, currentPath, tag):

        ManagerAbstract.__init__(self, currentPath, tag)

    @classmethod
    def command(cls):

        return 'sync'

    def execute(self):

        if not self.tag:
            print(Console.magenta('not ssh source given'))
            return

        dbFileName = ManagerAbstract._dbFileName

        process = Process('scp')
        process.startWithArguments(self.tag + ':' + dbFileName, dbFileName)

        if process.error:
            print(Console.red(process.error))
            return

        print(Console.green('done'))
