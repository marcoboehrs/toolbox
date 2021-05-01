#!/usr/bin/env python3
import sys;

if (len(sys.argv) != 2):
    sys.exit('Usage: {} string-to-convert'.format(sys.argv[0]));

result = ""
for c in sys.argv[1]:
    result+=str(hex(ord(c))).replace('0x','%');

print(result)
