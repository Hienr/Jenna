import queue, pafy, youtube_dl, vlc, threading, sys, os
from enum import Enum 

JobTypes = {'ADD':0,'PLAY':1,'PAUSE':2,'STOP':3,'EXIT':10}

jobQueue = queue.Queue()
def enqueue_job(job):
    jobQueue.put(job)


class Player:
    def __init__(self):
        self._player = vlc.MediaPlayer()
        self._video = None
        self._audiostream = None

    def setVideo(self, url):
        self._video = pafy.new(url)
        self._audiostream = self._video.getbestaudio()
        self._player.set_mrl(self._audiostream.url)

    def play(self):
        self._player.play()

    def pause(self):
        self._player.pause()
    
    def isPlaying(self):
        return self._player.isPlaying()
    
    def stop(self):
        self._player.stop()


class PlayerThread:
    def __init__(self):
        self.thread = threading.Thread(target=self._run, name='player-thread', daemon=True)
        self.thread.start()

    def _run(self):
        audiostream = Player()

        while True:
            # block on queue if its empty
            job = jobQueue.get()

            if (job[0] == JobTypes['ADD']):
                audiostream.setVideo(job[1])
            elif (job[0] == JobTypes['PLAY']):
                audiostream.play()
            elif (job[0] == JobTypes['PAUSE']):
                audiostream.pause()
            elif (job[0] == JobTypes['STOP']):
                audiostream.stop()
            elif (job[0] == JobTypes['EXIT']):
                os._exit(1)    

            jobQueue.task_done()
