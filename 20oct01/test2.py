#!/usr/bin/env python3

import sys

characters=["Luke", "Cody", "Leah", "Amidala", "Palpatine"]
types=["jedi","clone","general","senator","sith"]


for i in range(len(characters)):
	outstring="The type for {character:s} is {type:s}"
	print (outstring.format(character=characters[i],type=types[i]))