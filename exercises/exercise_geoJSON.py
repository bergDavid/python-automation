#google geolocation API
import urllib.request, urllib.error, urllib.parse
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
#while True:
#    address = input('Enter location: ')
#    if len(address) < 1: break
address = "Av. Agulhas Negras, s/n - Mangabeiras, Belo Horizonte - MG, 30210-060, Brazil"
address = "Ann Arbor, MI"
url = serviceurl + urllib.parse.urlencode({'address':address})
print('Retriving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrived',len(data),'characters')

try:
  js = json.loads(data)
except:
  js = None

if not js or 'status' not in js or js['status'] != 'OK':
  print("=== Failure to Retrive ===")
  print(data)
  quit()

print(json.dumps(js,indent=4))
lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lat"]
print("lat",lat,"lng",lng)
location = js['results'][0]['formatted_address']
print(location)
