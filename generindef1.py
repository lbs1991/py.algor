#!/usr/bin/python27

def genNum(x):
	y = 1
	while y <= x:
		yield y**2
		y += 1
g1 = genNum(9)
for i in g1:
	print i
