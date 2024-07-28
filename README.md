#SpotifyTimeMachine

In this project I use Beautiful Soup to parse the Billboard Top 100 songs list of a user provided date. Once I have the list of songs, I then use Spotipy package to authenticate with Spotify and search for the songs and retrieve their URI. There is error checking for if songs are not available. Once I have the song URIs I then create a playlist named for the user provided date. 
