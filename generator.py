#!/usr/bin/python27

l1 = ['a','b','c']
l2 = [1,2,3,4,5]

g1 = (i**2 for i in l2 if i>2)
for j in g1:
	print j
