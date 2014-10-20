#!/usr/bin/python27

str1 = 'abc'
str2 = 'qwe'
str3 = 'fgh'
largestr1 = '%s%s some %s\n' % (str1,str2,str3)
largestr2 = str1+str2+' some '+str3
print largestr1,largestr2
