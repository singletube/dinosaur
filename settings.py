from pygame import *
import random


init()



day_time = 500
score = 0
day_ch = 0
dino_speed = 1
size = (width, height) = (900, 350)  # windows' size
bg_image_night = image.load('images/bg_image.png')
bg_image_day = image.load('images/bg_image_day.png')
menu_pic = image.load('images/menu_pic.jpg')
fail_pic = image.load('images/fail_pic.jpg')
exit_exe = image.load('images/exit.png')
exit_exe = transform.scale(exit_exe, (50, 50))
day = bg_image_night
loud = image.load('images/speaker.png')
loud = transform.scale(loud, (50, 50))
silent = image.load('images/speaker_off.png')
silent = transform.scale(silent, (50, 50))
win = display.set_mode(size)
pos = height
music = True
otstup = 35

a = random.choice(['audio/Pixelizer.mp3', 'audio/Dance! .mp3', 'audio/Chiptune Your Head.mp3'])
mixer.music.load(a)

mixer.music.set_volume(0.1)
jump_sound = mixer.Sound('audio/jump_sound.mp3')

run_status = True
sneak_status = False
jump_status = False
jump_index = 30
gravity = 6
run_index = 2
sneak_index = 2
run_sprite = [image.load('images/green dino/run_Animation1.png'), image.load('images/green dino/run_Animation2.png')]
jump_sprite = image.load('images/green dino/dino.png')
sneak_sprite = [image.load('images/green dino/sneak1.png'), image.load('images/green dino/sneak2.png')]
sneaking_sprite = image.load('images/green dino/sneaking.png')
lost_sprite = image.load('images/green dino/lost.png')

# player parameters
dino_width = 42
dino_height = 44
pace = 70
x = 30
y = height - dino_height - 25
dino = image.load('images/green dino/dino.png')


cactus_sprite = image.load('images/cacti/cactus.png')
cactus_width = 38
cactus_height = 47
x1 = 800
y1 = y
cactus_array = []


"""menu const"""
distanse = 50
full_col = 255
null_col = 0