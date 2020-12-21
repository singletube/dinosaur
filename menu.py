import sys
import pygame
import settings

from Objects import *


init()





def dino_menu():
    global pos, music
    def draw():
        if music:
            screen.blit(loud, (width - 50, height - 50))
        else:
            screen.blit(silent, (width - 50, height - 50))
        text_x = width // 2 - 100
        pygame.draw.rect(screen, 'pink', (text_x, 200, 200, 70))
        font = pygame.font.Font('pixel font.ttf', 30)
        text = font.render(str('Начать'), 1, (0, 0, 0))
        screen.blit(text, (text_x + 20, 220))
        font = pygame.font.Font('pixel font.ttf', 40)
        text = font.render(str('Google динозавр'), 1, (255, 0, 0))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, pos - otstup))
        font = pygame.font.Font('pixel font.ttf', 40)
        text = font.render(str('Добро пожаловать'), 1, (255, 255, 255))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, pos))
        font = pygame.font.Font('pixel font.ttf', 30)
        text = font.render(str('Игра by Константин и Хаджимурад'), 1, (255, 255, 255))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, pos + otstup))
    pygame.init()
    pygame.display.set_caption('Запуск')
    size = width, height = 900, 350
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        if pos > height // 8:
            pos -= 10
        time.Clock().tick(pace)
        screen.blit(bg_image, (0, 0))
        draw()
        for event in pygame.event.get():
            keys = key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if (width // 2 - 100) < event.pos[0] < (width // 2 + 200) and 200 < event.pos[1] < 270:
                    return music
                if width - 50 < event.pos[0] and height - 50 < event.pos[1]:
                    if music:
                        screen.blit(silent, (width - 50, height - 50))
                        music = False
                    else:
                        screen.blit(loud, (width - 50, height - 50))
                        music = True




        pygame.display.flip()
        time.Clock().tick(pace)
    pygame.quit()