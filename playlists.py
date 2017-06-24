import sys
import spotipy
import pprint
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util
import constants

# manual input
# if len(sys.argv) < 3:
#     username = sys.argv[1]
#     playlist_id = sys.argv[2]
#     track_ids = sys.argv[3:]
#
# else:
#     sys.exit()

username = 'mlou15'
playlist_id = 'spotify:user:mlou15:playlist:5BMdRfsFPWO2zWIjEhY8ul'
track_ids = ['spotify:track:7BKLCZ1jbUBVqRi2FVlTVw']
scope = 'playlist-modify-public'
token = spotipy.util.prompt_for_user_token(username, scope, client_id='0b81334c2734457a83b8c35034dcd520', client_secret='a2c4ed680e244f96898b571f8a467', redirect_uri='https://mindylou.github.io')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print results
else:
    print "can't get token for " + username
