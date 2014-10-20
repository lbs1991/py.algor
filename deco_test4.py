#!/usr/bin/env pythin27

def log(func):
	def wrap(*a,**b):
		print 'call %s()' % func.__name__
		return func(*a,**b)
	return wrap
@log
def now():
	print '2014-9-25'

now()
print now.__name__

