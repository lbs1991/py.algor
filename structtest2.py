#!/usr/bin/python27

import struct

t1=(1,2,3)
buffer = apply(struct.pack,("ihb",)+t1)
print struct.unpack("ihb",buffer)
