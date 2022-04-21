#!/usr/bin/env python3

import os
from subprocess import run

from .manager_abstract import ManagerAbstract
from .console import Console

class ManagerSync(ManagerAbstract):

    def __init__(self, currentPath, tag):

        ManagerAbstract.__init__(self, currentPath, tag)

    @classmethod
    def command(cls):

        return 'sync'

    def execute(self):

        if not self.tag:
            print(Console.magenta('no ssh source given'))
            return

        dbFileName = ManagerAbstract._dbFileName

        result = run(['scp', self.tag + ':' + dbFileName,  dbFileName], capture_output=True)
        if result.stderr:
            print(Console.red(result.stderr))
            return

        print(Console.green('done'))
