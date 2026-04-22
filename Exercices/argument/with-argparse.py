#!/usr/bin/env python 
import argparse

parser = argparse.ArgumentParser(prog='balafon - python argument parser',description="numeric definition ")
parser.add_argument('command-name', help="command", type=str)
args = parser.parse_args()


print(args)


