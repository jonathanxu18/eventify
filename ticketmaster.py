import requests

from datetime import datetime, timedelta
from geopy import geocoders

geo = geocoders.GeoNames(username='jonathanxu18')

name, coor = geo.geocode('San Jose, CA')

coor = ','.join(map(str, coor))


current_date = datetime.now().replace(microsecond=0)
end_date = current_date + timedelta(days=185)
end_date = end_date.strftime('%Y-%m-%dT%H:%M:%SZ')

payload = {'keyword': 'odesza', 'endDateTime': end_date, 'radius': 500,
            'latlong': coor, 'apikey': 'yGC1IYG68FjPx6oeVFf2YAPw8nNRtMjt'}

api_url = 'https://app.ticketmaster.com/discovery/v2/events.json?'

response = requests.get(api_url, params=payload)

events = response.json()

for event in events['_embedded']['events']:
    print(event['name'], event['url'])

