#!/usr/bin/python27

list1 = ['jack','judy','born',111,222,333]
for i in list1 :
	if type(i) == type('a') : 
		proc = '{0[0.index(i)]:8}:{0[0.index(i)+3]:3}'.format(list1)
		print proc

