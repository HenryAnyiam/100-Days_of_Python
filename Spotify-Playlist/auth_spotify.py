#!/usr/bin/python3
"""authenticate with spotify"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas
import get_songs
from os import getenv


CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()['id']


data = pandas.read_csv("./top_songs.csv")
tracks = data.Songs.to_list()
artists = data.Artists.to_list()
tracks = tracks[0:100] if len(tracks) > 100 else tracks
artists = artists[0:100] if len(artists) > 100 else artists

year = get_songs.start_date
playlist = sp.user_playlist_create(user=user_id, name=f"Back to {year}",
                                   public="False",
                                   description=f"Songs from the year {year}")

playlist_tracks = []
for i, j in zip(tracks, artists):
    j = j.replace("Featuring ", "")
    j = j.replace(",", "").replace("&", "").replace("x", "")
    result = sp.search(q=f"track:{i} artist:{j}", type='track', limit=1)

    if result['tracks']['items']:
        playlist_tracks.append(result['tracks']['items'][0]['uri'])
    else:
        result = sp.search(q=f"track:{i}", type='track', limit=1)
        if result['tracks']['items']:
            playlist_tracks.append(result['tracks']['items'][0]['uri'])
        else:
            print(i, j)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'],
                            tracks=playlist_tracks)
print(playlist)