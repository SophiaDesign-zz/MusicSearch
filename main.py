
import spotipy
import spotipy.oauth2 as oauth2


client_id = '16625b3847fc451e89639d51bb77c22d'
client_secret = 'e8e7a0e4d35740dc89e2739c29ec5048'

auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)

from flask import Flask, render_template

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


# def path_to_image_html(path):
        #return '<img src="' + path + '"/>'

    #pd.set_option('display.max_colwidth', -1)

    #HTML(df.to_html(escape=False, formatters=dict(Image=path_to_image_html)))




#print(youtube_search('beyonce'))

if __name__ == '__main__':
    app.run(debug=True)
