print("\n\n****Local Gravity Calculator****")
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    json.dumps(js)

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    continue
    


import math as m
L = lat                                                                      #Latitude
H = int(input("Height at which you are from ground(in feet): "))             #Height from ground  
sinl = m.sin(L) ** 2 
sin2l = m.sin(2 * L) ** 2 
F = 9.780327 * ((1 + 0.0053024 * sinl) - (0.0000058 * sin2l))                #International Gravity Formula
z = 3.086 * (10 ** (-6)) * H                                                 #Free Air Correction
g = F - z                                                                    #Final g value
print("\n" + str(g) + " " + "m/s^2")