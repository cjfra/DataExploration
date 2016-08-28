__author__ = 'Guoguo'

from urllib import request


fhandle = request.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhandle:
    print(line.strip())