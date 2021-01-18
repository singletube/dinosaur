from settings import *
from random import *
import pygame

"""Главный класс врагов"""


class Enemies:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    """Функция спауна кактусов"""

    def cactus_spawn(self):
        global x, y
        if self.x >= -self.width:
            self.x -= dino_speed
            if self.x - x <= 20 and self.x - x >= 5:
                if y != self.y:
                    pass
                else:
                    return -1
        else:
            self.x = 2200
        win.blit(cactus_sprite, (self.x, self.y))

    def clear_by_class(self, cls):
        for sprite in self:
            if isinstance(sprite, cls):
                sprite.kill()


"""Дневной цикл, показывание счета, увеличение скорости"""


def win_actions(score):
    global win, run_status, pace, day, day_ch, dino_speed, cactus_array
    if day_ch % day_time == 0:
        if day == bg_image_day:
            day = bg_image_night
            dino_speed += 0.25
        else:
            day = bg_image_day
            dino_speed += 0.25
        day_ch += 1
    else:
        day_ch += 1
    win.blit(day, (0, 0))

    """Отображение счета"""

    font = pygame.font.Font('pixel font.ttf', 30)
    text = font.render(('score:' + str(score // 10)), 1, (255, 255, 255))
    win.blit(text, (650, 0))

    update()

    if run_status:
        running_animation()

        """Проверка на пригрыш"""

    if show_cactus_array(cactus_array) == -1:

        """Обновление игры"""

        dino_speed = 1
        day_ch = 1
        pace = 0
        cactus_array = []
        generate_cactus_array(cactus_array)
        day = bg_image_day
        return -1

    display.flip()


"""Функция прыжка"""


def jump():
    global y, jump_status, jump_index, gravity, pace
    if not sneak_status:
        win.blit(jump_sprite, (x, y))
    else:
        win.blit(sneaking_sprite, (x, y))
    if jump_index >= -30 and y <= 281:
        if jump_index == 30:
            mixer.Sound.play(jump_sound)
        jump_index -= 1
        if sneak_status and jump_index <= 0:
            y -= jump_index / (gravity / 3)
        else:
            y -= jump_index / gravity
    else:
        jump_index = 30
        y = 281
        jump_status = False


"""Функция проверки действия пользователя"""


def update():
    global jump_status, sneak_status, run_status
    keys = key.get_pressed()
    if (keys[K_SPACE] or keys[K_UP]) and not sneak_status:
        jump_status = True
    if keys[K_DOWN] or keys[KMOD_CTRL]:
        run_status = False
        sneak_status = True
        sneak_animation()
    if not keys[K_DOWN] and not keys[KMOD_CTRL]:
        run_status = True
        sneak_status = False
    if jump_status:
        jump()


"""Анимация бега динозавра"""


def running_animation():
    global run_index, run_status, win
    if run_index >= 16:
        run_index = 0
    if y == height - dino_height - 25:
        win.blit(run_sprite[run_index // 8], (x, y))
        run_index += 1


"""Анимация приседания"""


def sneak_animation():
    global sneak_status, sneak_index, run_status
    if sneak_index >= 16:
        sneak_index = 0
    if y == height - dino_height - 25:
        win.blit(sneak_sprite[sneak_index // 8], (x, y))
        sneak_index += 1


"""Алгаритм генерации кактусов"""


def generate_cactus_array(array):
    for i in range(400, 2200, 200):
        x1 = randint(i, i + 200)

        """Добавление врага(кактуса) в группу"""

        array.append(Enemies(x1, y, cactus_width, cactus_height))


"""Отрисовка кактусов"""


def show_cactus_array(array):
    for cactus in array:
        if cactus.cactus_spawn() == -1:
            return -1
