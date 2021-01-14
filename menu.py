from Objects import *

"""Функция главного меню"""


def dino_menu():
    global pos, music

    """Отрисовка объектов"""

    def draw():
        with open('records.txt', 'r', encoding='UTF-8') as line:
            line = line.readline()

            if music:
                screen.blit(loud, (width - distanse, height - distanse))
            else:
                screen.blit(silent, (width - distanse, height - distanse))
            text_x = width // 2 - distanse * 2
            pygame.draw.rect(screen, 'pink', (text_x, 200, 200, 70))
            font = pygame.font.Font('pixel font.ttf', 30)
            text = font.render(('Лучший счет:' + line), 1, (full_col, full_col, full_col))
            screen.blit(text, (0, pos + otstup * 2))
            text = font.render('Начать', 1, (null_col, null_col, null_col))
            screen.blit(text, (text_x + 20, 220))
            font = pygame.font.Font('pixel font.ttf', 40)
            text = font.render('Google динозавр', 1, (full_col, null_col, null_col))
            text_x = width // 2 - text.get_width() // 2
            screen.blit(text, (text_x, pos - otstup))
            font = pygame.font.Font('pixel font.ttf', 40)
            text = font.render('Добро пожаловать', 1, (full_col, full_col, full_col))
            text_x = width // 2 - text.get_width() // 2
            screen.blit(text, (text_x, pos))
            font = pygame.font.Font('pixel font.ttf', x)
            text = font.render('Игра by Константин и Хаджимурад', 1, (full_col, full_col, full_col))
            text_x = width // 2 - text.get_width() // 2
            screen.blit(text, (text_x, pos + otstup))

    pygame.init()
    pygame.display.set_caption('Запуск')
    size = width, height
    screen = pygame.display.set_mode(size)
    running = True

    """Гравный цикл меню"""

    while running:
        if pos > height // 8:
            pos -= 10
        time.Clock().tick(pace)
        screen.blit(menu_pic, (0, 0))
        draw()

        """Проверка действий пользователя"""

        for event in pygame.event.get():

            """Выход"""

            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:

                """Старт игры"""

                if (width // 2 - distanse * 2) < event.pos[0] < (width // 2 + distanse * 4) and distanse * 4 \
                        < event.pos[1] < 270:
                    return music

                """Включение / Отключение музыки"""

                if width - distanse < event.pos[0] and height - distanse < event.pos[1]:
                    if music:
                        screen.blit(silent, (width - distanse, height - distanse))
                        music = False
                    else:
                        screen.blit(loud, (width - distanse, height - distanse))
                        music = True

        pygame.display.flip()
        time.Clock().tick(pace)
    pygame.quit()
