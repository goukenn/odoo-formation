#!/usr/bin/env python
import sys

class CommandInfo:
    pass
class CommandArg:
    @staticmethod
    def ParseArg(*argv):
        pass

print('argument', len(sys.argv))

print(sys.argv[1:])
