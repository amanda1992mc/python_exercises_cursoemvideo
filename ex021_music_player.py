#tocar música do computador

from pygame import mixer
mixer.init()
mixer.music.load('Formation.mp3')
mixer.music.play()
mixer.music.stop()