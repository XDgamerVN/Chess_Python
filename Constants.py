import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
NEW_WIDTH = WIDTH
NEW_HEIGHT = HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SQ_SIZE = HEIGHT // 8
BUTTON_WIDTH = SQ_SIZE * 1.9
BUTTON_HEIGHT = SQ_SIZE / 2
PROMOTE_WIDTH = SQ_SIZE
PROMOTE_HEIGHT = SQ_SIZE * 4
FPS = 60  # For animations
images = {}
captures_images = {}
promote_images = {}
PIECE_SIZE = (SQ_SIZE, SQ_SIZE)
C_PIECE_SIZE = (SQ_SIZE // 2.6, SQ_SIZE // 2.6)
COLOR_A = ['#ebecd0', '#739552']
COLOR_Z = ['#739552', '#ebecd0']

# Tạo font
font_path = 'Arial'
small_font = pygame.font.SysFont(font_path, SQ_SIZE // 6, False, False)
medium_font = pygame.font.SysFont(font_path, SQ_SIZE // 4, True, False)
large_font = pygame.font.SysFont(font_path, SQ_SIZE // 3, False, False)

def load_images():
    """Initialize a global dictionary of images"""
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', 'bP',
              'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR', 'wP']
    for piece in pieces:
        images[piece] = (
            pygame.transform.smoothscale(pygame.image.load(f'images/{piece}.png'), PIECE_SIZE))

def load_captured_images():
    """Initialize a global dictionary of images"""
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', 'bP',  # Add 'bP'
              'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR', 'wP']  # Add 'wP'
    for piece in pieces:
        captures_images[piece] = (
            pygame.transform.smoothscale(pygame.image.load(f'images/{piece}.png'), C_PIECE_SIZE))

