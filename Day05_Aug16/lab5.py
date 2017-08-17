# pip install googlemaps
from googlemaps import Client
from datetime import datetime


api_key = 'your key'
gmaps = Client(api_key)
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
whitehouse_geoloc = gmaps.geocode(whitehouse)
print whitehouse_geoloc

destination = gmaps.reverse_geocode((38.897096, -77.036545))
print destination

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

lat_long = (gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lat'], gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lng'])
print lat_long
duke = gmaps.reverse_geocode(lat_long)[0]['formatted_address']
print duke 

local = gmaps.places('restaurant near ' + duke)
print local['results'][0]['formatted_address']
print local['results'][0]['name']

directions = gmaps.directions(duke, whitehouse)
print directions[0]['legs'][0]['distance']

for step in directions[0]['legs'][0]['steps']:
	print step['html_instructions']

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
destinations = []
directions = []
now = datetime.now()
for i in range(0, len(embassies)):
	destinations.append(gmaps.reverse_geocode(embassies[i])[0]['formatted_address'])
	directions.append(gmaps.directions(embassies[i], whitehouse, mode="transit", departure_time=now))
	print directions[i][0]['legs'][0]['distance']
# Answer: The second embassy is the closest. It is 0.8/1.6*1000 meters.

# what is its address?
embassy_B = destinations[1]
embassy_B # '1601 Massachusetts Ave NW, Washington, DC 20036, USA'

# if I wanted to hold a morning meeting there, which cafe would you suggest?
cafes = gmaps.places('cafe near ' + embassy_B)
print cafes['results'][0]['formatted_address'] # check one of them
print cafes['results'][0]['name']
# Compare the distances
for i in range(0, len(cafes)):
	cafe_address = cafes['results'][i]['formatted_address']
	print cafe_address
	test = gmaps.directions(embassy_B, cafe_address, mode="transit", departure_time=now) #Look up epoch time
	print test[0]['legs'][0]['distance'] #%cafes['results'][i]['name']
	print cafes['results'][i]['name']
# I would recommance this because it is the nearest:
#1625 Massachusetts Ave NW, Washington, DC 20008, United States
#{u'text': u'302 ft', u'value': 92}
#Galley Cafe

# if I wanted to hold an evening meeting there, which bar would you suggest? 
bars = gmaps.places('bar near ' + embassy_B)
print bars['results'][0:len(bars)]['formatted_address'] # check one of them
print bars['results'][0:len(bars)]['name']
# Compare the ratings
for i in range(0, len(bars)):
	bar_address = bars['results'][i]['formatted_address']
	print bar_address
	#test = gmaps.directions(embassy_B, bar_address, mode="transit", departure_time=now)
	print bars['results'][i]['rating'] #%cafes['results'][i]['name']
	print bars['results'][i]['name']
# I would recommand this because it has the highest rating.
#300 Massachusetts Ave NW, Washington, DC 20001, United States
#4.5
#Carving Room Kitchen & Bar
