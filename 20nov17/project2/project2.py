#!/usr/bin/env python3
# Github link: https://github.com/Jak1022/FSU-BCH5884-Fall2020/tree/master/20nov17/project2
# Created by Yudan for BCH 5884 project 2

import sys
import numpy as np
from matplotlib import pyplot as plt

if len(sys.argv) !=2:
	print("Usage: <project2.py> <chromatogram_file.asc> ")
	print("I'll find peaks in the chromatogram for you.")
	sys.exit()

# Parse the chromatogram file

data=sys.argv[1]
f=open(data)
lines=f.readlines()
f.close()

time=[]
absorbance=[]
z=0
for line in lines[3:]:
    words=line.split()
    try:
        time.append(float(words[0]))
        absorbance.append(float(words[1]))
    except:
        print ("Parsing Complete!")
        continue

# Find peaks (4 major peaks in total)
# da = derivative of absorbance
da=np.gradient(absorbance)        
threshhold=1.5
peaks=[[[]]]+[[[]]]

# p is peak number
# z is for determing the position when da[n]*da[n+1] <0, z=0 for first time da cross -threshhold, z=1 for second time. Peak will end at z=1
p=0
n=0
z=0
while n+1 < len(time):
# peak start point
	if da[n]>threshhold:
		while True:
			peaks[0][p].append(time[n])
			peaks[1][p].append(absorbance[n])
# peak end point
			if da[n]>-threshhold and z==1:
				z=0
				p+=1
				peaks[0]+=[[]]
				peaks[1]+=[[]]
				break
			elif da[n]<-threshhold and z==0:
				z=1
				n+=1
				continue
			n+=1
	n+=1

num=0
# define color dictionary
color={0:'ro',1:'g+',2:'ms',3:'y^'}
while num+1<len(peaks[0]):
# begin = staring point of the peak
# end = ending point of the peak
# tp = time of the maximum absorbance
	begin=peaks[0][num][0]
	end=peaks[0][num][-1]
	a=np.array(peaks[1][num])
	maximum=a.max()
	tp=peaks[0][num][a.argmax()]
	print ("peak%3d  begins at %.3f minute and ends at %.3f minute with a maximum absorbance of %.3f mAU, at time %.3f minute" %((num+1),begin,end,maximum,tp))
	plt.plot(peaks[0][num],peaks[1][num],color[num])
	num+=1

plt.plot(time,absorbance)
plt.xlabel('Time (min)')
plt.ylabel('Absorbance (mAU)')
plt.show()