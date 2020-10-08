#!/usr/bin/env python3
#Created by Yudan Chen for Programming Course

import sys

pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()

column=[]
for line in lines:
	words=line.split()
	atomserial=int(words[1]),str(words[2]),str(words[3]),str(words[4]),int(words[5]),float(words[6]),float(words[7]),float(words[8]),float(words[9]),float(words[10]),str(words[11])
	column.append(atomserial)

f.close()


f=open("tmp2.out",'w')
for temp in column:
	s="Atom {0}\n"
	f.write(s.format(temp))
f.close()




print("Done!")