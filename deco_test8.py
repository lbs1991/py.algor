#!/usr/bin/env python27
import functools
def log(text):
	def deco(func):
		@functools.wraps(func)
		def wrapper(*a,**b):
			print 'begin call'
			print '%s %s()' % (text,func.__name__)
			func(*a,**b)
			print 'after call'
		return wrapper
	return deco

@log('execute')
def now():
	print '2014-9-25'

now()
