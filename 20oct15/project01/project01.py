#!/usr/bin/env python3
# Created by Yudan Chen for BCH5884 Project 1
# Github link:

import sys
import math


# STEP 1: read the pdb file

pdbfilename=sys.argv[1]

f=open(pdbfilename)
lines=f.readlines()
f.close()

records=[]
massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0, "P":30.97, "S":32.07,"MG":24.30}
for line in lines:
	atomdict={}
	
	# item1 = column 1 of the pdbfile - ATOM
	item1=str(line[0:5])
	   
	# item2 = column 2 of the pdbfile - atom serial number          
	item2=str(line[6:11])
	
	# item3 = column 3 of the pdbfile - atom name			  
	item3=str(line[12:16])
	
	# item4 = column 4 of the pdbfile - residue name			 
	item4=str(line[17:20])
	
	# item5 = column 5 of the pdbfile - chain identifier
	item5=str(line[21])
	
	# item6 = column 6 of the pdbfile - residue sequence number
	item6=int(line[22:26])
	
	# x = column 7 of the pdbfile - x coordinates
	x=float(line[30:38])
	
	# y = column 8 of the pdbfile - y coordinates
	y=float(line[39:46])
	
	# z = column 9 of the pdbfile - z coordinates
	z=float(line[47:54])
	
	# item7 = column 10 of the pdbfile - occupancy
	item7=float(line[55:60])
	
	# item8 = column 11 of the pdbfile - temperature factor
	item8=float(line[61:66])
	
	# element = column 12 of the pdbfile - element
	element=line[76:78].strip()
	
	# mass = mass of the element
	mass=massdict[element]
	records.append([item1,item2,item3,item4,item5,item6,x,y,z,item7,item8,element,mass])


# STEP 2: calculation for center mass coordinates

summass=0
sumxmass=0
sumymass=0
sumzmass=0

for record in records:
	summass+=record[12]
	sumxmass+=record[12]*record[6]
	sumymass+=record[12]*record[7]
	sumzmass+=record[12]*record[8]

cmx=sumxmass/summass
cmy=sumymass/summass
cmz=sumzmass/summass


# STEP 3: create a new textfile (pdbfile), and write data.

f=open("project01out.pdb",'w')
for atom in records:
	s="{0:6}{1:6}{2:5}{3:4}{4:1}{5:4}{6:12.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}{11:>12}\n"
	f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6]-cmx,atom[7]-cmy,atom[8]-cmz,atom[9],atom[10],atom[11]))
f.close()

	
print("Done!")