#!/usr/bin/env python3

import os

from .manager_abstract import ManagerAbstract

from .process import Process
from .console import Console


class ManagerRepo(ManagerAbstract):

    def __init__(self, currentPath, tag):

        ManagerAbstract.__init__(self, currentPath, tag)

    @classmethod
    def command(cls):

        return 'repo'

    def execute(self):

        if not self.tag:
            print(Console.magenta('not tag given'))
            return

        giturl = Process.execute(['git', 'config', '--get', 'remote.origin.url'])
        if not giturl:
            print(Console.red('not a git repository'))
            return

        giturl = giturl.decode().strip()
        self.data[ManagerAbstract.RepoKey][self.tag] = giturl
        print('stored ' + Console.yellow(self.tag) + ' @ ' + giturl)
        self.save()
