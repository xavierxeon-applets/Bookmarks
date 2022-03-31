#!/usr/bin/env python3

import os

from .manager_abstract import ManagerAbstract

from .console import Console


class ManagerList(ManagerAbstract):

    def __init__(self, currentPath, tag):

        ManagerAbstract.__init__(self, currentPath, tag)

    @classmethod
    def command(cls):

        return 'list'

    def execute(self):

        if self.data[ManagerAbstract.DirKey]:
            print('available bookmarks:')
            for tag, path in self.data[ManagerAbstract.DirKey].items():
                if os.path.exists(path):
                    print(' * ', Console.green(tag), path)
                else:
                    print(' * ', Console.magenta(tag), path)

        if self.data[ManagerAbstract.RepoKey]:
            print('available repositories:')
            for tag, repoUrl in self.data[ManagerAbstract.RepoKey].items():
                print(' * ', Console.green(tag), repoUrl)
