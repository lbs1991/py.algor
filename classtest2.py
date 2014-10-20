#!/usr/bin/python27

class Class1():
	data = 'hehe1'
	def __init__(self,x):
		self.vk = x
	print 'haha2'
	def printInfo(self):
		print self.data
		print self.vk
ins1 = Class1('good')
ins1.printInfo()


