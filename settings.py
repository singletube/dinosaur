from pygame import *
import random

init()

"""Константы для главного меню"""

distanse = 50
full_col = 255
null_col = 0

"""Загрузка Изображений"""
bg_image_night = image.load('images/bg_image.png')
bg_image_day = image.load('images/bg_image_day.png')
menu_pic = image.load('images/menu_pic.jpg')
fail_pic = image.load('images/fail_pic.jpg')
exit_exe = image.load('images/exit.png')
run_sprite = [image.load('images/green dino/run_Animation1.png'),
              image.load('images/green dino/run_Animation2.png')]
jump_sprite = image.load('images/green dino/dino.png')
sneak_sprite = [image.load('images/green dino/sneak1.png'),
                image.load('images/green dino/sneak2.png')]
sneaking_sprite = image.load('images/green dino/sneaking.png')
lost_sprite = image.load('images/green dino/lost.png')
dino = image.load('images/green dino/dino.png')
cactus_sprite = image.load('images/cacti/cactus.png')
silent = image.load('images/speaker_off.png')
loud = image.load('images/speaker.png')

"""Загрузка Звуков"""

"""Можно добавить в папку для рандомного воспроизведения,
 удалить ненужные"""

a = random.choice(['audio/Pixelizer.mp3', 'audio/Dance! .mp3',
                   'audio/Chiptune Your Head.mp3'])

jump_sound = mixer.Sound('audio/jump_sound.mp3')

"""Изменяемые параметры игры"""
"""Время длительности дня/ночи"""
day_time = 1000

"""Начальная скорость"""
dino_speed = 1

"""Параметры кактусов"""
cactus_width = 38
cactus_height = 47

"""Параметры динозавра"""
dino_width = 42
dino_height = 44

"""Громкость музыки"""
mixer.music.set_volume(0.1)

"""Начальное время суток"""

day = bg_image_night

"""Константы"""
size = (width, height) = (900, 350)
score = 0
day_ch = 0
jump_index = 30
gravity = 6
run_index = 2
sneak_index = 2
pace = 70
x = 30
y = height - dino_height - 25
pace = 70
x = 30
y = height - dino_height - 25
x1 = 800
y1 = y
otstup = 35

"""Настройка параметров"""
mixer.music.load(a)
exit_exe = transform.scale(exit_exe, (50, 50))
loud = transform.scale(loud, (50, 50))
silent = transform.scale(silent, (50, 50))
win = display.set_mode(size)
pos = height
cactus_array = []

"""Включение/Выключение"""
run_status = True
sneak_status = False
jump_status = False
music = True
