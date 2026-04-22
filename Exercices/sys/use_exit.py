import sys
import importlib
from typing import NoReturn

def igk_die(*argv, **kwargs) -> NoReturn :
    # old way to dynamically import 'sys'
    # __import__('sys').exit()
    # a way to dynamically import a module 
    # importlib.import_module('sys').exit()
    # direct module call 
    sys.exit(*argv, **kwargs)


i = 10
while i > 5:
    i -= 1
    if i == 8:
        igk_die(87)
    print(fr'item {i}')
