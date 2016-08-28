__author__ = 'Guoguo'

import urllib.request
import bs4

url = 'http://python-data.dr-chuck.net/comments_218916.html'

html = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(html, "lxml" )

tags = soup('span')
numcount = 0
numsum = 0

for tag in tags:
    numsum += int(tag.contents[0])
    numcount = numcount + 1

print(numsum)
print(numcount)
