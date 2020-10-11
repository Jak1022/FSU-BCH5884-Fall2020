#!/usr/bin/env python3

import sys

pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()

column=[]
for line in lines:
	words=line.split()
	atomserial=str(words[0]),str(words[1]),str(words[2]),str(words[3]),str(words[4])
	atomname=str(words[2])
	residuename=str(words[3])
	chainID=str(words[4])
	residuenumber=int(words[5])
	xcoordinate=float(words[6])
	ycoordinate=float(words[7])
	zcoordinate=float(words[8])
	occupancy=float(words[9])
	tempfact=float((words[10]))
	element=str(words[11])
	#print("Atom",atomserial,atomname,residuename,chainID,residuenumber,xcoordinate,ycoordinate,zcoordinate,occupancy,tempfact,element)
	column.append(atomserial)
	#column.append(atomname)
	#column.append(residuename)
	#column.append(chainID)
	#column.append(residuenumber)
	#column.append(xcoordinate)
	#column.append(ycoordinate)
	#column.append(zcoordinate)
	#column.append(occupancy)
	#column.append(tempfact)
	#column.append(element)
	#sys.exit()
f.close()


f=open("tmp.out",'w')
for atominfo in column:
	s="{0:6} {1:5} {2:4} {3:3} {4:1}\n"
	f.write(s.format(atominfo[0],atominfo[1],atominfo[2],atominfo[3],atominfo[4]))
f.close()

print("Done!")