__author__ = 'Guoguo'

import urllib.request
import bs4

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for num in range(1,count+1):
    html = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "lxml" )
    tags = soup('a')
    # print(tags[position-1].get('href'))
    url = tags[position-1].get('href')

print(tags[position-1].contents[0])