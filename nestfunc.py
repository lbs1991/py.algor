#!/usr/bin/python27

def f1():
	x = 3
	def f2():
		y = 'haha'
		print x,y
	return f2
'''
#fi = f1()
#fi()
'''
f1()()
