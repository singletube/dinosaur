import sys
import time
from pygame import *
from settings import *
from Objects import *
from menu import dino_menu
from records import record_check


init()
if dino_menu():
    mixer.music.play(-1)
else:
    pass
generate_cactus_array(cactus_array)
while True:
    pace += 0.01
    score += 1
    for event_ in event.get():
        if event_.type == QUIT:  # exit game
            record_check(score // 10)
            sys.exit(0)


    win_actions()
    time.Clock().tick(pace)


