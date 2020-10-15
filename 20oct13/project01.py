#!/usr/bin/env python3
# Created by Yudan Chen for Project 1 (FSU Programming Course Fall 2020)
#GitHub link:

import sys
pdaname=sys.argv[1]
f=open(pdaname,'r')
lines=f.readlines()

column=[]
for line in lines:
	if line[:4]=="ATOM":
		words=line.split()
		atominfo=str(line[0:5]),str(line[6:11]),str(line[12:16]),str(line[17:20]),str(line[21]),int(line[22:26]),float(line[30:38]),float(line[39:46]),float(line[47:54]),float(line[55:60]),float(line[61:66]),str(line[77:78])
		print(atominfo)
		column.append(atominfo)
f.close()

f=open("project01.pdb",'w')
for atom in column:
	s="{0:6}{1:6}{2:5}{3:4}{4:1}{5:4}{6:12.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}{11:>12}\n"
	f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6],atom[7],atom[8],atom[9],atom[10],atom[11]))
f.close()

	
print("Done!")