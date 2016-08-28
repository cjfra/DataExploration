from urllib import request
import json

serviceurl = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'

print ('Retrieving', serviceurl)
json_data = request.urlopen(serviceurl).read()
print ('Retrieved',len(json_data),'characters')


js = json.loads(json_data.decode(encoding='UTF-8'))

print(js)