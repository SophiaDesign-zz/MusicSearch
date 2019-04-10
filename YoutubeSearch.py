#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..
from pprint import pprint

import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyBuuyVwd2iMSY-_R2R39ISVVmAEkDzqGNE'
#DEVELOPER_KEY = 'AIzaSyAh_EdKpTwjno1az-UBV8awwmhW5MgrDK8'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

#search_term = input('Search for music: ')

def youtube_search(user_input):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    #q=options.q,
    q = str(user_input),
    part='id,snippet',
    maxResults=10
  ).execute()

  videos = []
  video_id = []
  video_link = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.

  image_link = search_response['items'][0]['snippet']['thumbnails']['high']['url']
  pprint(image_link)

  #variables to add into html page

  #search results
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      #videos.append('{} ({})'.format(search_result['snippet']['title'],
        #                         search_result['id']['videoId'])
      #videos.append('{}'.format(search_result['snippet']['title']))
      video_link.append('https://www.youtube.com/embed/{}'.format(search_result['id']['videoId']))
      video_id.append('{}'.format(search_result['id']['videoId']))


  #print ('Videos:\n', '\n'.join(videos), '\n')
  # returns also the id, which can be used for hyperlink youtube.com/watch?v=[replace with id]

  #pprint(video_id)
  #pprint(video_link)
  pprint(videos)


  return [image_link,
          videos,
          video_id
          ]



if __name__ == '__main__':
#   parser = argparse.ArgumentParser()
#   parser.add_argument('--q', help='Search term', default='Google')
#   parser.add_argument('--max-results', help='Max results', default=1)
#   args = parser.parse_args()

  try:
    youtube_search('queen')
  except HttpError:
    print ('An HTTP error occurred:\n')