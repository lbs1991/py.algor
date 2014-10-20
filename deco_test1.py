#!/usr/bin/python27

def deco(func):
	def say():
		print 'say'
		func()
		print 'bye'
	return say

@deco
def show():
		print 'pig'
#def time()
show()
