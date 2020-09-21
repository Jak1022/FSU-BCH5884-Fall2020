#!/usr/bin/env python3
#Here is the link to my GitHub repository: https://github.com/Jak1022/FSU-BCH5884-Fall2020/blob/master/20sep17/Triangle_angles.py

import math

#enter x and y coordinates/values for each point
ax=float(input("Please enter the x-axis value of point A: "))
ay=float(input("Please enter the y-axis value of point A: "))
bx=float(input("Please enter the x-axis value of point B: "))
by=float(input("Please enter the y-axis value of point B: "))
cx=float(input("Please enter the x-axis value of point C: "))
cy=float(input("Please enter the y-axis value of point C: "))

#calculating distance between points
distanceAB=math.sqrt((ax-bx)**2+(ay-by)**2)
distanceAC=math.sqrt((ax-cx)**2+(ay-cy)**2)
distanceBC=math.sqrt((bx-cx)**2+(by-cy)**2)

print("Distance between AB: ")
print(distanceAB)
print("Distance between AC: ")
print(distanceAC)
print("Distance between BC: ")
print(distanceBC)

#calculating angles using cosine law
#alpha is the angle between AB and AC; beta is the angle between AB and BC; gamma is the angle between AC and BC.
alpha=math.acos(((distanceAB)**2+(distanceAC)**2-(distanceBC)**2)/(2*(distanceAB)*(distanceAC)))*180/math.pi
beta=math.acos(((distanceAB)**2+(distanceBC)**2-(distanceAC)**2)/(2*(distanceAB)*(distanceBC)))*180/math.pi
gamma=math.acos(((distanceAC)**2+(distanceBC)**2-(distanceAB)**2)/(2*(distanceAC)*(distanceBC)))*180/math.pi

#results
print("Angles of alpha (degrees): ")
alpha=round(alpha,1)
print(alpha)
print("Angles of beta (degrees): ")
beta=round(beta,1)
print(beta)
print("Angles of gamma (degrees): ")
gamma=round(gamma,1)
print(gamma)

print("Done!")
