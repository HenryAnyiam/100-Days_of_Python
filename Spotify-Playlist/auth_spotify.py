#!/usr/bin/python3
"""authenticate with spotify"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="6b192c9888d54de7ac345f1437d75049",
                                               client_secret="2a2ea00dd9454054a82837e02c0d7275",
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()['id']


data = pandas.read_csv("./top_songs.csv")
tracks = data.Songs.to_list()
artists = data.Artists.to_list()

playlist = sp.user_playlist_create(user=user_id, name="Back in Time",
                                   public="False", description="Songs from the year 2016")

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