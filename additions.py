from interface import *
from constants import *
import pygame

def quit_game(SQ_SIZE):
    """Kiểm tra xem người chơi có muốn thoát game hay không"""
    in_quit = True
    while in_quit:
        # Vẽ nút và các thông báo thoát game
        draw_button("", 0,SQ_SIZE * 4, SQ_SIZE * 3,
                    SQ_SIZE * 6, SQ_SIZE * 2, SQ_SIZE // 7, SQ_SIZE // 15,
                    'white', 'black', COLOR_SCREEN, COLOR_SCREEN, 'aquamarine')

        draw_button('Are you sure you want to quit the game?', SQ_SIZE // 3, SQ_SIZE * 7 - SQ_SIZE // 4,
                    SQ_SIZE * 3 + SQ_SIZE // 2, SQ_SIZE // 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                    'white', 'white', COLOR_SCREEN, COLOR_SCREEN, COLOR_SCREEN)

        yes_button = draw_button("Yes", SQ_SIZE // 3, SQ_SIZE * 5 + SQ_SIZE // 8, SQ_SIZE * 4 + SQ_SIZE // 4,
                                 SQ_SIZE * 2 - SQ_SIZE // 4, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                                 'white', 'black', COLOR_SCREEN, 'tomato', 'tomato')

        no_button = draw_button("No", SQ_SIZE // 3, SQ_SIZE * 7 + SQ_SIZE // 8, SQ_SIZE * 4 + SQ_SIZE // 4,
                                SQ_SIZE * 2 - SQ_SIZE // 4, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                                'white', 'black', COLOR_SCREEN, 'light green', 'light green')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if no_button.collidepoint(event.pos):
                    return
                elif yes_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        clock.tick(60)
        pygame.display.flip()

def draw_button(text, text_size,  x, y, width, height, border_radius, border_width,
                not_text_hover_color, text_hover_color, not_hover_color, hover_color, border_color):
    """Vẽ nút bo góc với màu sắc, viền và vị trí đã chỉ định"""
    font_button = pygame.font.SysFont('Arial', text_size, True)
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    if button_rect.collidepoint(mouse_pos):
        button_color = hover_color
        text_color = text_hover_color
    else:
        button_color = not_hover_color
        text_color = not_text_hover_color
    draw_rounded_rect(screen, button_rect, border_radius, border_color, border_width)
    rounded_rect(screen, button_rect, border_radius, button_color)
    text_surface = font_button.render(text, True, text_color)
    screen.blit(text_surface, text_surface.get_rect(center=button_rect.center))
    return button_rect

def rounded_rect(surface, rect, radius, color):
    """Vẽ hình chữ nhật bo góc"""
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_rounded_rect(surface, rect, radius, color, border_width):
    """Vẽ hình chữ nhật bo góc với viền"""
    border_rect = rect.inflate(border_width, border_width)
    pygame.draw.rect(surface, color, border_rect, border_radius=radius)
