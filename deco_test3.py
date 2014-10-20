#!/usr/bin/python27

def deco(func):
	def say(x):
		print 'say'
		func(x)
		print 'bye'
	return say

@deco
def show(x):
		print x
#def time()
#show('pig')
show()
