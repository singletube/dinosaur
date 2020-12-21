from pygame import *
import random

init()  # launch library

win = display.set_mode((1000, 700))  # open playing window; there are x y coordinates in brackets
# player parameters
x = 50
y = 50
width = 40
height = 40
pace = 100

flag = True
while flag:
    time.delay(100 // pace)  # cycle life
    for event_ in event.get():
        if event_.type == QUIT:  # exit game
            flag = False
    # movements
    keys = key.get_pressed()
    if keys[K_LEFT] and x > 5:
        x -= 2
    elif keys[K_RIGHT] and x < 995 - width:
        x += 2
    elif keys[K_DOWN] and y < 695 - height:
        y += 2
    elif keys[K_UP] and y > 5:
        y -= 2
    
    win.fill((0, 0, 0))
    draw.rect(win, (255, 50, 119), (x, y, width, height))
    display.update()