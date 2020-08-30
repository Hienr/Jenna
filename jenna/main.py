import player
import time
url = "https://www.youtube.com/watch?v=gFFOXwniVKw"

audiostream = player.Player() 

audiostream._setVideo(url)
audiostream._play()
