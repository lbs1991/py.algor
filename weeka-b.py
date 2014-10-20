#!/usr/bin/python27

l1=[0,1,2,3,4,5,6]
l2=[0,1,2,5]
l3=[]
for i in range(len(l1)):
	count=0
	for j in range(len(l2)):   
		if	l1[i]==l2[j]:	
			break
		else:
			count=count+1
	if count==4:
		l3.append(l1[i])
print l3
