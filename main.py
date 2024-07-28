# import required libraries
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Set up the environment variables
load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# get the date from the user and create the url
date = input("Enter the date in the format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

# get the site and parse it
response = requests.get(url)
site = response.text
soup = BeautifulSoup(site, "html.parser")
song_elements = soup.select(selector=".o-chart-results-list__item h3")
songs = [song.getText().strip() for song in song_elements]

# authenticate the user
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]

# search for the songs in Spotify
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# create the playlist and add the songs
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Playlist created successfully.")