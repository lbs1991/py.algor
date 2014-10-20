#!/usr/bin/python27

l1=[1,2,3,4,5,6,7]
l2=[3,7,9]

for i in l2:
	if i in l1:
		l1.remove(i)
print l1
