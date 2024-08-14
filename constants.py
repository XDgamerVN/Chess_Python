import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 820
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Chess by Nguyen Le Van Dung')
font = pygame.font.SysFont('roboto', 20)
medium_font = pygame.font.SysFont('roboto', 22)
big_font = pygame.font.SysFont('roboto', 40)
timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_pieces = white_pieces
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []

# Tải trong hình ảnh mảnh trò chơi (Nữ hoàng, Vua, Tân binh, Giám mục, Hiệp sĩ, Cầm đồ) x 2
def load_and_scale_image(piece_color, piece_name, size):
    image = pygame.image.load(f'assets/images/{piece_color}_{piece_name}.png')
    return pygame.transform.scale(image, size)

# Danh sách các quân cờ và màu sắc
pieces = ['queen', 'king', 'rook', 'bishop', 'knight', 'pawn']
colors = ['black', 'white']

# Tạo các hình ảnh và hình ảnh nhỏ cho cả quân đen và quân trắng
images = {color: {piece: load_and_scale_image(color, piece, (100, 100)) for piece in pieces} for color in colors}
small_images = {color: {piece: load_and_scale_image(color, piece, (50, 50)) for piece in pieces} for color in colors}

# Truy cập hình ảnh quân trắng
white_queen = images['white']['queen']
white_queen_small = small_images['white']['queen']
white_king = images['white']['king']
white_king_small = small_images['white']['king']
white_rook = images['white']['rook']
white_rook_small = small_images['white']['rook']
white_bishop = images['white']['bishop']
white_bishop_small = small_images['white']['bishop']
white_knight = images['white']['knight']
white_knight_small = small_images['white']['knight']
white_pawn = images['white']['pawn']
white_pawn_small = small_images['white']['pawn']

# Truy cập hình ảnh quân đen
black_queen = images['black']['queen']
black_queen_small = small_images['black']['queen']
black_king = images['black']['king']
black_king_small = small_images['black']['king']
black_rook = images['black']['rook']
black_rook_small = small_images['black']['rook']
black_bishop = images['black']['bishop']
black_bishop_small = small_images['black']['bishop']
black_knight = images['black']['knight']
black_knight_small = small_images['black']['knight']
black_pawn = images['black']['pawn']
black_pawn_small = small_images['black']['pawn']

# tạo phong cấp cho tốt quân
white_promotions = ['bishop', 'knight', 'rook', 'queen']
black_promotions = white_promotions

# Xác định vị trí chưa di chuyển
white_moved = [False] * len(white_pieces)
black_moved = [False] * len(black_pieces)

# Vị trí cả quân đen, vị trí cả quân trắng
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
check = False
castling_moves = []


