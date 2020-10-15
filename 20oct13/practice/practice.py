#!/usr/bin/env python3
# Created by Yudan Chen for Project 1 (FSU Programming Course Fall 2020)
# GitHub link:

import sys
import math
import numpy


# STEP 1
# read pdbfile
pdaname=sys.argv[1]
f=open(pdaname,'r')
lines=f.readlines()

column=[]
for line in lines:
	if line[:4]=="ATOM":
		words=line.split()
		atominfo=str(line[0:5]),str(line[6:11]),str(line[12:16]),str(line[17:20]),str(line[21]),int(line[22:26]),float(line[30:38]),float(line[39:46]),float(line[47:54]),float(line[55:60]),float(line[61:66]),str(line[77:78])
		column.append(atominfo)	
f.close()


# STEP 2
# calculating the center of mass
# mass=mass of the element
# mx=mass*xcoordinate, my=mass*ycoordinate, mz=mass*zcoordinate

calcinfo=[]
for a in column:
	if a[11]=="N":
		mass=14.01
		mx=mass*a[6]
		my=mass*a[7]
		mz=mass*a[8]
		
	if a[11]=="C":
		mass=12.01
		mx=mass*a[6]
		my=mass*a[7]
		mz=mass*a[8]
		
	if a[11]=="O":
		mass=16.00
		mx=mass*a[6]
		my=mass*a[7]
		mz=mass*a[8]
	ss=float(mx),float(my),float(mz),float(mass)
	calcinfo.append(ss)
	

# STEP 3
# write those mx, my, mz, and mass to a new textfile
# the content of the textfile is [mx, my, mz, mass]
f=open("test.out",'w')
for atom in calcinfo:
	s="{0:10.3f}{1:10.3f}{2:10.3f}{3:>8.2f}\n"
	f.write(s.format(atom[0],atom[1],atom[2],atom[3]))
f.close()


# STEP 4
# sum mx, my, mz, mass
# then, calculate center mass x, y, z coordinates (cmx, cmy, cmz)

a = numpy.genfromtxt("test.out",usecols=[0,1,2,3])
sss=a.sum(axis=0)

#print(sss[0],sss[3])

cmx=sss[0]/sss[3] # center mass x-coordinate
cmy=sss[1]/sss[3] # center mass y-coordinate
cmz=sss[2]/sss[3] # center mass z-coordinate

print(cmx,cmy,cmz)


# STEP 5
# create another new textfile (pdb format)
# write each component in the row for every element
# for x, y, z coordinate, conduct calculate to find final values for each coordinate using the cmx, cmy, cmz we got in STEP 4
# final x coordinate = original x coordinate - cmx
# final y coordinate = original y coordinate - cmy
# final z coordinate = original z coordinate - cmz

f=open("practice.pdb",'w')
for atom in column:
	s="{0:6}{1:6}{2:5}{3:4}{4:1}{5:4}{6:12.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}{11:>12}\n"
	f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6]-cmx,atom[7]-cmy,atom[8]-cmz,atom[9],atom[10],atom[11]))
f.close()

	
print("Done!")