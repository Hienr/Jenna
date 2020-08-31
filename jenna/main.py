import player, api
from collections import namedtuple 
from player import JobTypes
from api import YouTubeAPI

youtubeAPI = api.YouTubeAPI()

Job = namedtuple('Job', 'id url')

url = "https://www.youtube.com/watch?v=gFFOXwniVKw"

player_thread = player.PlayerThread()

while True:
    action = int(input("Action: "))

    if (action == JobTypes['ADD']):
        player.enqueue_job((action, url))
    elif (action == 11):
        search_results = youtubeAPI.search_by_keyword(input("Keyword: "))

        for item in search_results.values():
            print(item)
        
        keys_list = list(search_results)
        
        url = "https://www.youtube.com/watch?v=" + keys_list[int(input("Pick an item: "))]
        player.enqueue_job((0, url))
    else:
        player.enqueue_job((action, None))