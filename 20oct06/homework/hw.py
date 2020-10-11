#!/usr/bin/env python3
#Created by Yudan Chen for Programming Course

import sys

pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()

column=[]
for line in lines:
	words=line.split()
	atominfo=str(words[0]),int(words[1]),str(words[2]),str(words[3]),str(words[4]),int(words[5]),float(words[6]),float(words[7]),float(words[8]),float(words[9]),float(words[10]),str(words[11])
	print("ATOM",atominfo)
	column.append(atominfo)
f.close()


f=open("hw.out",'w')
for atom in column:
	s="{0:6} {1:5} {2:4} {3:3} {4:1} {5:3} {6:8.3f} {7:8.3f} {8:8.3f} {9:6} {10:6}       {11:2}\n"
	f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6],atom[7],atom[8],atom[9],atom[10],atom[11]))
f.close()




print("Done!")