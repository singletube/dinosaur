from Objects import *
from menu import dino_menu
from records import record_check
from retry import retry_menu

init()

if dino_menu():
    mixer.music.play()
else:
    pass

"""Проверка включения музыки в игре"""

generate_cactus_array(cactus_array)

pygame.display.set_caption('Играем')

"""Главный игровой цикл"""

while True:
    pace += 0.01
    score += 1
    """Функция выхода/проигрыша"""
    for event_ in event.get():
        if event_.type == QUIT:
            record_check(score // 10)
            # Проверка на рекорд
            retry_menu(score // 10)
            score = 0

    """Проверка на проигрыш"""

    if win_actions(score) == -1:
        record_check(score // 10)
        # Проверка на рекорд
        retry_menu(score // 10)
        score = 0
        init()

        """Обновление экрана"""

    time.Clock().tick(pace)
