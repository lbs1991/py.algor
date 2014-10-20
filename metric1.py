#!/usr/bin/python27

m1 = [ 	[1,2,3],
		[11,12,13],
		[21,22,23],
		[31,32,33]	]
mt = [ [row[i] for row in m1] for i in range(3)]
print mt
