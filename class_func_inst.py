#!/usr/bin/python27

class MyClass():
	def __init__(self,x):
		self.v = x
	def func1(self):
		print("haha",self.v)
	
inst1 = MyClass(3)
inst1.func1()
