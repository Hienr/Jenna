import player
from collections import namedtuple 
from player import JobTypes
import os 

from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=os.environ.get('YOUTUBE_API'))

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()

print(response)

Job = namedtuple('Job', 'id url')

url = "https://www.youtube.com/watch?v=gFFOXwniVKw"

player_thread = player.PlayerThread()

while True:
    action = int(input("Action: "))

    if (action == JobTypes['ADD']):
        player.enqueue_job((action, url))
    else:
        player.enqueue_job((action, None))