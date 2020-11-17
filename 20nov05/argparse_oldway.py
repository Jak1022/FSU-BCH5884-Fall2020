#!/usr/bin/env python3

import sys
import argparse

if len(sys.argv) !=3:
	print("usage: argparse.py <number1> <number2>")
	print("I'll add two numbers passed from the command line")
	sys.exit()

a=sys.argv[1]
c=sys.argv[2]
sum=a+c

print("the sum is", sum)