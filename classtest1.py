#!/usr/bin/python27

class ClassTest():
	data = 'haha1'
	def setinfo(self,x):
		self.str = x
	def getinfo(self):
		print self.str

ins1 = ClassTest()
print ins1.data 
ins1.setinfo('hehe2')
print ins1.str
ins1.getinfo()
