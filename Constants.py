import pygame as p

p.init()
version = "v0.3 Beta"

CHESS_BOARD = 700

WIDTH = CHESS_BOARD * 1.55
HEIGHT = CHESS_BOARD * 1.16
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Chess by Dũng")
DIMENSION = 8  # Dimensions of a chess board are 8x8
SQ_SIZE = CHESS_BOARD // DIMENSION
BUTTON_WIDTH = SQ_SIZE * 2
BUTTON_HEIGHT = SQ_SIZE / 2
PROMOTE_WIDTH = SQ_SIZE
PROMOTE_HEIGHT = SQ_SIZE * 4
FPS = 60  # For animations
images = {}
captures_images = {}
promote_images = {}
PIECE_SIZE = (SQ_SIZE, SQ_SIZE)
C_PIECE_SIZE = (SQ_SIZE // 1.75, SQ_SIZE // 1.75)
COLOR_A = ['#ebecd0', '#739552']
COLOR_Z = ['#739552', '#ebecd0']

# Tạo font
font_path = 'Arial'
small_font = p.font.SysFont(font_path, CHESS_BOARD // 45, False, False)
medium_font = p.font.SysFont(font_path, CHESS_BOARD // 35, True, False)
large_font = p.font.SysFont(font_path, CHESS_BOARD // 20, False, False)
version_font = p.font.SysFont(font_path, CHESS_BOARD // 30, False, False)

def load_images():
    """Initialize a global dictionary of images"""
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', 'bP',
              'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR', 'wP']
    for piece in pieces:
        images[piece] = (
            p.transform.smoothscale(p.image.load(f'images/{piece}.png'), PIECE_SIZE))

def load_captured_images():
    """Initialize a global dictionary of images"""
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', 'bP',  # Add 'bP'
              'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR', 'wP']  # Add 'wP'
    for piece in pieces:
        captures_images[piece] = (
            p.transform.smoothscale(p.image.load(f'images/{piece}.png'), C_PIECE_SIZE))
