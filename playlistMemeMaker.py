import sys
import spotipy
import pprint
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util
import constants

"""
Searches Spotify for a song with the exact title.

Returns:
Spotify ID of a track with the input title.

Parameters:
title: String, name of the song that should be searched for on Spotify
sp: Spotify session client
"""
def findSongWithTitle(title, sp):
    offset = 0
    max_offset = 200
    while (offset < max_offset):
        results = sp.search(q=title, type='track', limit=50, offset=offset)
        if len(results['tracks']['items']) == 0:
            return ''
        for item in results['tracks']['items']:
            if item['name'].lower() == title:
                return str(item['id'])
        offset += 50
    return ''

"""
Finds songs with titles matching the given sentence input and adds them
to a new playlist.

Parameters:
sentence: String
sp: Spotify session client
"""
def makeMemeSongList(sentence, sp):
    words = sentence.split()
    song_list = []
    for index in range(0, len(words)):
        print(words[index])
        track_id = findSongWithTitle(words[index], sp)
        if track_id == '':
            # if at the end, no way to string words together
            if index == len(words)-1:
                return ''
            # try stringing words together and try again
            words[index+1] = words[index] + ' ' + words[index+1]
        else:
            song_list.append(track_id)
    return song_list

def main():
    username = 'mlou15'
    scope = 'playlist-modify-public'

    token = spotipy.util.prompt_for_user_token(username, scope=scope, client_id=constants.CLIENT_ID, client_secret=constants.CLIENT_SECRET, redirect_uri=constants.REDIRECT_URI)
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        sentence = raw_input('Enter a phrase: ')
        playlist_name = raw_input('Enter a playlist title: ')
        song_list = makeMemeSongList(sentence, sp)
        print(song_list)
        playlist = sp.user_playlist_create(username, playlist_name)
        playlist_id = playlist["id"]
        songs = sp.user_playlist_add_tracks(username, playlist_id, song_list)

    else:
        print "can't get token for " + username

if __name__ == '__main__':
    main()
