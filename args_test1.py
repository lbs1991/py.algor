#!/usr/bin/python27

#def fun1(a,b,c):
def fun1(*s):
	sum = 0
	for i in s:
		sum += i
		
	return sum


print fun1(*(1,2,3))
