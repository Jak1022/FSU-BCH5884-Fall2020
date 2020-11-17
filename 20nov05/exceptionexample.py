#!/usr/bin/env python3

numbers=0
avg=0

while True:
	inp=input("please give me a number or the world 'done': ")
	
	if inp=="done":
		break
	else:
		x=float(inp)
		avg+=x
		numbers+=1
	
avg=avg/numbers
print("the average is %.2f" % (avg))