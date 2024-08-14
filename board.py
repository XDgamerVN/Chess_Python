import pygame
from constants import *

# vẽ bảng trò chơi chính
def draw_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, '#ebecd0', [i * 100, j * 100, 100, 100])
            else:
                pygame.draw.rect(screen, '#739552', [i * 100, j * 100, 100, 100])
        pygame.draw.line(screen, 'grey', [910, 740], [910, 0], 3)
        pygame.draw.line(screen, 'grey', [800, 810], [0, 810], 20)
        pygame.draw.line(screen, 'grey', [810, 840], [810, 0], 20)
        status_text = ['White turn', 'White turn', 'Black turn', 'Black turn']
        if turn_step < 2:
            pygame.draw.rect(screen, 'black', [820, 740, 820, 740])
            screen.blit(big_font.render(status_text[turn_step], True, '#e9e9e9'), (840, 770))
        else:
            pygame.draw.rect(screen, 'white', [820, 740, 820, 740])
            screen.blit(big_font.render(status_text[turn_step], True, '#545454'), (840, 770))
        # Vẽ chữ hàng
        for i in range(8):
            text = medium_font.render(chr(ord('A') + i), True, 'black')
            screen.blit(text, (15 + i * 100 + 100 // 3, 803))

        # Vẽ chữ cột
        for i in range(8):
            text = medium_font.render(str(8 - i), True, 'black')
            screen.blit(text, (807, 10 + i * 100 + 100 // 3))
