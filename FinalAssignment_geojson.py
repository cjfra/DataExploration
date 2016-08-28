from urllib import request
import urllib.parse
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'


location = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': location})
print ('Retrieving', url)
json_data = request.urlopen(url).read()
print ('Retrieved',len(json_data),'characters')


try: js = json.loads(json_data.decode(encoding='UTF-8'))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print ('==== Failure To Retrieve ====')


place_id = js["results"][0]["place_id"]
print ('Place id is: ', place_id)