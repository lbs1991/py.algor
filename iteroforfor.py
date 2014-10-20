#!/usr/bin/python27

l1 = ['x','y','z']
l2 = [1,2,3]

l3 = [(i,j) for i in l1 for j in l2]
print l3
