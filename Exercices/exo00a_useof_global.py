#!/usr/bin/env python 

x = 12
y = 23

def xam():
    # separated global with ","
    global x, y 
    return x + y


def withNonLocal():
    # global y
    def _subDefinition():
        nonlocal x, y 
        return x * y
    x = 55
    y = 5
    return _subDefinition()

print(xam())

print(withNonLocal())
