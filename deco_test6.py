#!/usr/bin/env python27
import functools
def log(text):
	def deco(func):
		@functools.wraps(func)
		def wrapper(*a,**b):
			print '%s %s()' % (text,func.__name__)
			return func(*a,**b)
		return wrapper
	return deco

@log('execute')
def now():
	print '2014-9-25'

now()
