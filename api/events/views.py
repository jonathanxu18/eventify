import spotipy
import requests

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from geopy import geocoders
from spotipy.oauth2 import SpotifyOAuth
from time import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'events/index.html')

def login_spotify(request):

    cache_handler, auth_manager = get_OAuth(request)

    # We are redirecting from the authorization link
    if 'code' in request.GET:
        auth_manager.get_access_token(request.GET['code'])
        return JsonResponse({'token_info': cache_handler.get_cached_token()})

    # Check if we have a token cached in the session
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()
        return JsonResponse({"auth_url": auth_url})

    # If the user is signed-in, then we want to display the city selector
    del request.session['token_info']
    return HttpResponse("This is the login page")

def display_events(request):

    _, auth_manager = get_OAuth(request)
    artists = get_artists(auth_manager)

    coordinates = get_coordinates(request.GET.get('city'))

    end_date = get_end_date()

    start = time()

    events = []

    for artist in artists:

        payload = {'keyword': artist, 'endDateTime': end_date, 'radius': 500,
                    'latlong': coordinates, 'apikey': 'yGC1IYG68FjPx6oeVFf2YAPw8nNRtMjt'}

        api_url = 'https://app.ticketmaster.com/discovery/v2/events.json?'

        response = requests.get(api_url, params=payload)

        results = response.json()

        if '_embedded' in results:
            for event in results['_embedded']['events']:
                print(event['name'], event['url'])
                events.append(event['url'])

    end = time()

    print(f'time: {end-start}')

    return JsonResponse({'artists': artists, 'events': events})

def get_artists(auth_manager):
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results = sp.current_user_top_artists(limit=50)

    artists = []

    for artist in results['items']:
        artists.append(artist['name'])
    
    return artists

def get_coordinates(city):
    geo = geocoders.GeoNames(username='jonathanxu18')

    _, coor = geo.geocode(city)

    coor = ','.join(map(str, coor))

    return coor

def get_end_date():
    current_date = datetime.now().replace(microsecond=0)
    end_date = current_date + timedelta(days=365)
    end_date = end_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    print(end_date)

    return end_date

def get_OAuth(request):
    cache_handler = spotipy.cache_handler.DjangoSessionCacheHandler(request)
    auth_manager = SpotifyOAuth(scope='user-top-read', 
                                cache_handler=cache_handler)
    
    return cache_handler, auth_manager

