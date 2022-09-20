import spotipy

from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read'

auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.current_user_top_artists(limit=50)

for artist in results['items']:
    print(artist['name'])



