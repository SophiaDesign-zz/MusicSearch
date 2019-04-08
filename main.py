# from YoutubeSearch import youtube_search
# from SpotifySearch import UserInput
# from SpotifySearch import SearchSpot

from flask import Flask, render_template
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from YoutubeSearch import youtube_search

app = Flask(__name__)


@app.route('/')
def home():
    # grab my api data
    return render_template('search.html')


@app.route('/results/<user_input>')
def results(user_input):
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

print(youtube_search('beyonce'))

if __name__ == '__main__':
    app.run(debug=True)
