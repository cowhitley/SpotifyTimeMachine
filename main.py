# import required libraries
from bs4 import BeautifulSoup
import requests

# get the date from the user and create the url
date = input("Enter the date in the format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

# get the site and parse it
response = requests.get(url)
site = response.text
soup = BeautifulSoup(site, "html.parser")
song_elements = soup.select(selector=".o-chart-results-list__item h3")
songs = [song.getText().strip() for song in song_elements]

