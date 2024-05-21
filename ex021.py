import time
from pygame import mixer, event

mixer.init()
mixer.music.load('C418 - Alpha (Minecraft Volume Beta) (128 kbps).mp3')
mixer.music.play()

while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
