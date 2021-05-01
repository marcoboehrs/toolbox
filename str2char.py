#!/usr/bin/env python3
import sys

def showUsage():
    sys.exit('Usage:\n'
             '{} format string-to-converti\n\n'
             'format:\n'
             '-u urlencode\n'
             '-j javascript CharCode'.format(sys.argv[0]));

def urlencode(input):
    result = ""
    for c in input:
        result+=str(hex(ord(c))).replace('0x','%');
    return result

def javascriptCharCode(input):
    result = ""
    for c in input:
        result+=str(hex(ord(c)))+',';
    return result[:-1]


if (len(sys.argv) != 3):
    showUsage()

if (sys.argv[1] == '-u'):
    print(urlencode(sys.argv[2]))
    exit()

if (sys.argv[1] == '-j'):
    print(javascriptCharCode(sys.argv[2]))
    exit()

if (sys.argv[1] == '-h'):
    showUsage()

showUsage()
