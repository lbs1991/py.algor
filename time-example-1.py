#!/usr/bin/python27

import time
now_sec = time.time()
now_form1 = time.gmtime()
now_form2 = time.gmtime(now_sec)
nowlocal = time.localtime()
print now_sec
print now_form1
print now_form2
print nowlocal
