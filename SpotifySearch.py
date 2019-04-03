import spotipy
import spotipy.oauth2 as oauth2
import sys
import pprint
import numpy as np
import pandas as pd

client_id = '16625b3847fc451e89639d51bb77c22d'
client_secret = 'e8e7a0e4d35740dc89e2739c29ec5048'

auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)

def UserInput():
    Asktosearch = str(input('What are you looking for?'))
    return Asktosearch

def SearchSpot():
    while True:
        popular = []
        name = []
        artists = []
        r = UserInput()
        results = spotify.search(q=r, limit=25) #searches for the string that the user inputs
        for i, t in enumerate(results['tracks']['items']): #add data to the lists hopefully and adds a numbers them
            popular.append(t['popularity'])
            name.append(t['name'])
            artists.append(t['artists'][0]['name'])
        arrays = [np.array(name),np.array(artists)] #to make an array with both song names and song artists
        ser = pd.Series(popular,index=arrays) #uses Pandas package to construct a Series, with the index being arrays
        serOrder = pd.Series.sort_values(ser,ascending=False)
        print(serOrder)

SearchSpot()

#results = spotify.search(q='artist:ja rule', type='artist')
#print(results)

