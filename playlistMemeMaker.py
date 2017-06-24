import sys
import spotipy
import pprint
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util
import constants

'''
Searches Spotify for a song with the exact title.

Returns:
Spotify ID of a track with the input title.

Parameters:
title: String, name of the song that should be searched for on Spotify
'''
def findSongWithTitle(title):
    offset = 0
    max_offset = 200
    while (offset < max_offset):
        results = sp.search(q="'"+title+"'", type='track', limit=50, offset=offset)
        if len(results['tracks']['items']) == 0:
            return ''
        for item in results['tracks']['items']:
            if item['name'].lower() == title:
                return item['id']
        offset += 50

"""
Finds songs with titles matching the given sentence input and adds them
to a new playlist.

Parameters:
sentence: String
"""
def makeMemeSongList(sentence):
    words = sentence.split()
    song_list = []
    for index in range(0, len(words)-1):
        track_id = findSongWithTitle(words[index])
        if track_id == '':
            # try stringing words together and try again
            words[index+1] = words[index] + ' ' + words[index+1]
        else:
            song_list.append(track_id)
    return song_list

def main():
    username = 'mlou15'
    scope = 'playlist-modify-public playlist-modify-private'
    playlist_name = 'new playlist for you'

    token = spotipy.util.prompt_for_user_token(username, scope=scope, client_id=constants.CLIENT_ID, client_secret=constants.CLIENT_SECRET, redirect_uri=constants.REDIRECT_URI)
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlist = sp.user_playlist_create(username, playlist_name)
        sentence = "this is a test"
        song_list = makeMemeSongList(sentence)
        songs = sp.user_playlist_add_songs(username, playlist, song_list)

    else:
        print "can't get token for " + username

if __name__ == '__main__':
    main()
