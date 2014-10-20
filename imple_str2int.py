#!/usr/bin/env python27

def str2num(s):
	d1 = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	def smap(s):
		return d1[s]
	for i in s:
		if(d1.has_key(i) and isinstance(d1[i],int)):
			flag = 1
		else:
			flag = 0
			print('wrong input!') 
			break
	if(flag):
		print reduce(lambda x,y :x*10+y, map(smap,s))
flag = 0
while not flag:			
	s = raw_input('please enter a number:')
	str2num(s)

