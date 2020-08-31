import player
import time
import queue
import threading
from collections import namedtuple 
from player import JobTypes
Job = namedtuple('Job', 'id url')

url = "https://www.youtube.com/watch?v=gFFOXwniVKw"

player_thread = player.PlayerThread()

while True:
    action = int(input("Action: "))

    if (action == JobTypes['ADD']):
        player.enqueue_job((action, url))
    else:
        player.enqueue_job((action, None))