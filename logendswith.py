#!/usr/bin/python27
import os
filelist1 = os.listdir('/var/log')
filelist2 = [ i for i in filelist1 if i.endswith('.log')]
print filelist2
