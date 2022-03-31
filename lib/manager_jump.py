#!/usr/bin/env python3

import os
import sys
from pathlib import Path

from .console import Console

from .manager_abstract import ManagerAbstract


class ManagerJump(ManagerAbstract):

    _jumpFile = str(Path.home()) + '/.bookmarks/jump'
    _JumpExitCode = 33

    def __init__(self, currentPath, tag):

        ManagerAbstract.__init__(self, currentPath, tag)

    @classmethod
    def command(cls):

        return 'jump'

    def execute(self):

        if not self.tag:
            self.jumpSelection()
            return

        self._jumpInternal(self.tag)

    def jumpSelection(self):

        index = 1
        tagDict = dict()
        for tag, path in self.data[ManagerAbstract.DirKey].items():
            if not os.path.exists(path):
                continue
            tagDict[index] = (tag, path)
            index = index + 1

        if not tagDict:
            print(Console.blue('no bookmarks available'))
            return

        for index, data in tagDict.items():
            print(Console.yellow(str(index)), ':', data[0], Console.grey(data[1]))

        selection = input(Console.green('select number '))
        try:
            index = int(selection)
        except ValueError:
            index = None

        if not index in tagDict:
            print(Console.magenta('invalid selection'))
            return

        gotoTag = tagDict[index][0]
        self._jumpInternal(gotoTag)

    def _jumpInternal(self, gotoTag):

        if not gotoTag in self.data[ManagerAbstract.DirKey]:
            print(Console.magenta('tag not stored'), ':', gotoTag)
            return

        path = self.data[ManagerAbstract.DirKey][gotoTag]
        if not os.path.exists(path):
            print(Console.red('direcotry does not exists'), ':', path, 'for tag', gotoTag)
            return

        with open(ManagerJump._jumpFile, 'w') as outfile:
            outfile.write(path)

        sys.exit(ManagerJump._JumpExitCode)
