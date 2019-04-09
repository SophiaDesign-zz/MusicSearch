#from YoutubeSearch import youtube_search
#from SpotifySearch import SearchSpot
import spotipy
import spotipy.oauth2 as oauth2
import sys
import pprint
import numpy as np
import pandas as pd
from IPython.display import Image, HTML



client_id = '16625b3847fc451e89639d51bb77c22d'
client_secret = 'e8e7a0e4d35740dc89e2739c29ec5048'

auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)

from flask import Flask, render_template
#from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError
#from YoutubeSearch import youtube_search
#from SpotifySearch import SearchSpot
from basic import SearchSpotify

app = Flask(__name__)


@app.route('/')
def home():
    # grab my api data
    return render_template('search.html')


#@app.route('/results/<user_input>')
#def results(user_input):
    youtube_results = youtube_search(user_input)
    video_id = youtube_results[2][0]
    video_link = "https://www.youtube.com/embed/{}".format(video_id)

    #image_url = ['snippet.thumbnails.(key).url']
    image_url = youtube_results[0]
    image = '{}'.format(image_url)

    return render_template('results.html',
                           image = image_url,
                           title = youtube_results[1],
                           user_input = user_input,
                           video_link = video_link,
                           )

@app.route('/spotifyresult/<user_input>')
def SearchSpot(user_input):
    while True:
        popular = []
        name = []
        artists = []
        Album =[]
        theImage =[]
        preview = []


        r = str(user_input)
        results = spotify.search(q=r, limit=10) #searches for the string that the user inputs
        for i, t in enumerate(results['tracks']['items']): #add data to the lists hopefully and adds a numbers them
            results = spotify.search(q=r, limit=10)
            popular.append(t['popularity'])
            name.append(t['name'])
            artists.append(t['artists'][0]['name'])
            Album.append(t['album']['name'])
            theImage.append(t['album']['images'][0]['url'])
            #theImage.append('<img src="{}">'.format(t['album']['images'][0]['url']))
            preview.append(t['preview_url'])
        arrays = [np.array(name),np.array(artists), np.array(Album), np.array(theImage),np.array(preview)] #to make an array with both song names and song artists
        ser = pd.Series(popular,index=arrays) #uses Pandas package to construct a Series, with the index being arrays
        serOrder = pd.Series.sort_values(ser,ascending=False)
        df = pd.DataFrame(data= arrays)
        df = df.T
        spotresults = HTML(df.to_html(escape=False))


        img_links = np.array(theImage)
        url = []


        for image_link in img_links:
            url.append('<img src="{}">'.format(image_link))





        print(spotresults)


        return render_template('spotifyresults.html',
                                   result = spotresults,
                                   img = np.array(theImage),
                               song = np.array(name).tolist(),
                               tables=[spotresults]

                                   )

# def path_to_image_html(path):
        #return '<img src="' + path + '"/>'

    #pd.set_option('display.max_colwidth', -1)

    #HTML(df.to_html(escape=False, formatters=dict(Image=path_to_image_html)))




#print(youtube_search('beyonce'))

if __name__ == '__main__':
    app.run(debug=True)
