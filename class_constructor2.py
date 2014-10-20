#!/usr/bin/python27

class Constructor():
	def __init__(self,voice='hi'):
		self.voice = voice
	def __del__(self):
		pass
	def say():
		print "haha"
	
ins1 = Constructor()
print ins1.voice
ins2 = Constructor('good')
print ins2.voice
print Constructor.__module__
