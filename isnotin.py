#!/usr/bin/python27

x = [x for x in range(1,10)]
print(x)
y =[]
 
result = True if 12 not in x else False  # this is  the best way
print(result)
result = True if not 12 in x else False  # this way just like as " (not 12) in x"
print(result)
  
print(x is y)
print(x is not y) # this is the best way
print(not x is y) # this way just like as " (not x ) is y" ,so upper is the best way
   
result = 2 if 1 < 2 else 5 if 4 > 5 else 6 # just as 1 > 2 ? 2 : 4 > 5 ? 5 : 6
print(result)
