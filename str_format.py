#!/usr/bin/env python27

l1 = ['name','age','sex']
l2 = ['lbs',23,'M']
d1 = {'name':'lbs','age':23,'sex':'M'}
str1 = 'what is your {0} ? it is {1}.'
for v1,v2 in zip(l1,l2):
	print str1.format(v1,v2)
for vi,v2 in zip(d1.keys(),d1.values()):
	print str1.format(v1,v2)
	
