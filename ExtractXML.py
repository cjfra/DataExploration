__author__ = 'Guoguo'

from urllib import request
import xml.etree.ElementTree as ET

#serviceurl = 'http://python-data.dr-chuck.net/comments_42.xml'
url = input("Enter location: ")
uh = request.urlopen(url)
print ('Retrieving', url)

data = uh.read()
print ('Retrieved',len(data),'characters')

root = ET.fromstring(data)
print (root.find('note').text)
lst_note = root.findall("comments/comment")

sum = 0
count = 0
for item in lst_note:
    sum += int(item.find('count').text)
    count += 1

print('Count: ', count)
print('Sum: ', sum)