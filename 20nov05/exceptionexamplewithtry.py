#!/usr/bin/env python3

numbers=0
avg=0

while True:
	inp=input("please give me a number or the world 'done': ")
	
	try:
		x=float(inp)
		avg+=x
		numbers+=1
		
	except ValueError:
		if inp=="done":
			break
		else:
			print("incorrect value entered. please enter a number or 'done'")

try:
	avg=avg/numbers
except ZeroDivisionError:
	print("zero numbers entered; please try again")
else:
	# executes of the try completes without exception
	print("the average is %.2f" % (avg))