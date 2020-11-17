#!/usr/bin/env python3

import sys
import argparse

parser=argparse.ArgumentParser(description="A program to illustrate command line argument parsing")
parser.add_argument('numbers', type=int, nargs='+', help="a set of numbers")

args=parser.parse_args()
print(dir(args))
print(args.numbers)
