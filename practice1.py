#!/usr/bin/python27

strin = '/etc/passwd'
strou = '/tmp/test2'
f1 = open(strin,'r')
f2 = open(strou,'w')
#def kk():
for i in f1.readlines():
	f2.write(str(i.split(':'))+'\n')
f1.close()
f2.close()
