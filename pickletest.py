#!/usr/bin/python27

import pickle
#d1 = {'a':61,'c':63,'lbs':9999}
d1 = {'q':22,'w':33}
f1 = open('/root/test','a+')
pickle.dump(d1,f1)
f1.close()
f2 = open('/root/test','r+')
d2 = pickle.load(f2)
f2.close()
print d2
