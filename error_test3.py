#!/usr/bin/python27
import sys
class MyError(Exception):
	def __init__(self,value):
		self.value = value
#if type(sys.argv[1]) != typr('a'):
def try_except(x):
	try:
		#raise MyError(2*2)
		raise MyError(x)
	except MyError as e:
		print('my exception occurred:',e.value)
	
try:
	x = int(sys.argv[1])
	try_except(x)
except:
	x = sys.argv[1]
	try_except(x)
