#!/usr/bin/env python3

import os

from .manager_abstract import ManagerAbstract

from .console import Console


class ManagerStore(ManagerAbstract):

    def __init__(self, currentPath, tag):

        ManagerAbstract.__init__(self, currentPath, tag)

    @classmethod
    def command(cls):

        return 'store'

    def execute(self):

        if not self.tag:
            print(Console.magenta('not tag given'))
            return

        self.data[ManagerAbstract.DirKey][self.tag] = self.currentPath
        print('stored ' + Console.yellow(self.tag) + ' @ ' + self.currentPath)
        self.save()
