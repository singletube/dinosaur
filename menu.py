import pygame
import settings
from Objects import *



def dino_menu():
    global pos, music
    def draw():
        if music:
            screen.blit(loud, (width - distanse, height - distanse))
        else:
            screen.blit(silent, (width - distanse, height - distanse))
        text_x = width // 2 - distanse * 2
        pygame.draw.rect(screen, 'pink', (text_x, 200, 200, 70))
        font = pygame.font.Font('pixel font.ttf', 30)
        text = font.render(str('Начать'), 1, (null_col, null_col, null_col))
        screen.blit(text, (text_x + 20, 220))
        font = pygame.font.Font('pixel font.ttf', 40)
        text = font.render(str('Google динозавр'), 1, (full_col, null_col, null_col))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, pos - otstup))
        font = pygame.font.Font('pixel font.ttf', 40)
        text = font.render(str('Добро пожаловать'), 1, (full_col, full_col, full_col))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, pos))
        font = pygame.font.Font('pixel font.ttf', x)
        text = font.render(str('Игра by Константин и Хаджимурад'), 1, (full_col, full_col, full_col))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, pos + otstup))
    pygame.init()
    pygame.display.set_caption('Запуск')
    size = width, height
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        if pos > height // 8:
            pos -= 10
        time.Clock().tick(pace)
        screen.blit(bg_image, (0, 0))
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if (width // 2 - distanse * 2) < event.pos[0] < (width // 2 + distanse * 4) and distanse * 4\
                        < event.pos[1] < 270:
                    return music
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