#!/usr/bin/env python3
# Created by Yudan Chen for BCH 5884 RDMS homework
# Github link: https://github.com/Jak1022/FSU-BCH5884-Fall2020/tree/master/20oct29/RMSDhomework

import sys
from math import sqrt

def readpdb(pdbfilename):
	"""Parse pdb and return records as a list of dictionaries"""
	pdbfile=open(pdbfilename,'r')
	lines=pdbfile.readlines()
	pdbfile.close()
	
	#parse the pdb
	records1=[]
	for line in lines:
		if line[:4]=="ATOM" or line[:6]=="HETATM":
			d={}
			d['rtype']=line[0:6]
			d['atomnumber']=int(line[6:11])
			d['atomtype']=line[12:16]
			d['altloc']=line[16:17]
			d['residue']=line[17:20]
			d['chain']=line[21:22]
			d['residuenumber']=int(line[22:26])
			d['icode']=line[26:27]
			d['x']=float(line[30:38])
			d['y']=float(line[38:46])
			d['z']=float(line[46:54])
			d['occupancy']=float(line[54:60])
			d['tempfact']=float(line[60:66])
			d['element']=line[76:78].strip()
			d['charge']=line[78:80].strip()
			d['mass']=getmass(d['element'])
			records1.append(d)
	
	return records1
	
def getmass(element):
	"""Determine mass for element type"""
	massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0,"P":30.97,"S":32.07,"MG":24.30}
	mass=massdict.get(element)
	return mass
	
def rmsd(pdbfile1,pdbfile2):
    """Take two lists from the two pdbs and calculate RMSD"""
    rmsdsum=0
    n=len(pdbfile1)
    for atom in range(len(pdbfile1)):
        dx=(pdbfile1[atom]['x']-pdbfile2[atom]['x'])**2
        dy=(pdbfile1[atom]['y']-pdbfile2[atom]['y'])**2
        dz=(pdbfile1[atom]['z']-pdbfile2[atom]['z'])**2
        rmsdsum+=(dx+dy+dz)
    tot_rmsd=sqrt(rmsdsum/n)
    return tot_rmsd

if __name__=="__main__":
    """Perform the RMSD calculation with previously defined functions above"""
    pdb1=readpdb("2FA9noend.pdb") 
    pdb2=readpdb("2FA9noend2mov.pdb")
    rmsd=rmsd(pdb1,pdb2)
    print ("The RMSD for these two input pdb files is %.3f" % rmsd)
