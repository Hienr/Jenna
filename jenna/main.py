import pafy
import youtube_dl
import vlc
url = "https://www.youtube.com/watch?v=gFFOXwniVKw"

video = pafy.new(url)                                                                                                                       
audiostream = video.getbestaudio()

player = vlc.MediaPlayer(audiostream.url)
# player = vlc.MediaPlayer("F:\Music\한국 음악\Cinderella Time - NC.A.mp3")
player.play()

print(video.title)
print(video.duration)
# print(video.rating)
# print(video.author)
# print(video.length)
# print(video.keywords)
print(video.thumb)
# print(video.videoid)
# print(video.viewcount)
while True : pass