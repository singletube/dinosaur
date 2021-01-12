import pygame
import settings
from Objects import *





def retry_menu(score):
    global pos, music
    def draw():
        with open('records.txt', 'r', encoding='UTF-8') as line:
            line = line.readline()
            screen.blit(exit_exe, (width - distanse, height - distanse))
            text_x = width // 2 - distanse * 2
            pygame.draw.rect(screen, 'pink', (text_x, 200, 200, 70))
            font = pygame.font.Font('pixel font.ttf', 30)
            text = font.render(('Лучший счет:' + line), 1, (0, 0, 255))
            screen.blit(text, (0, pos + otstup * 2))
            text = font.render(('Текущий:' + str(score)), 1, (0, 0, 255))
            screen.blit(text, (0, pos + otstup * 3))
            text = font.render('Заного', 1, (null_col, null_col, null_col))
            screen.blit(text, (text_x + 20, 220))
            text = font.render('Вы проиграли', 1, (0, 0, 255))
            text_x = width // 2 - text.get_width() // 2
            screen.blit(text, (text_x, pos))
    pygame.init()
    pygame.display.set_caption('Проиграли')
    size = width, height
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        if pos > height // 8:
            pos -= 10
        time.Clock().tick(pace)
        screen.blit(fail_pic, (0, 0))
        screen.blit(exit_exe, (width - distanse, height - distanse))
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:
                if (width // 2 - distanse * 2) < event.pos[0] < (width // 2 + distanse * 4) and distanse * 4\
                        < event.pos[1] < 270:
                    pass
                if width - distanse < event.pos[0] and height - distanse < event.pos[1]:
                    raise SystemExit






        pygame.display.flip()
        time.Clock().tick(pace)
    pygame.quit()

retry_menu(500)