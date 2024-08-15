import pygame
import chess

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")

# Thiết lập kích thước quân cờ và quân cờ nhỏ
PIECE_SIZE = (100, 100)
SMALL_PIECE_SIZE = (25, 25)

# Kích thước ô vuông trên bàn cờ
SQUARE_SIZE = 100

# Định nghĩa các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Thiết lập kích thước ô vuông trên bàn cờ
SQUARE_SIZE = SCREEN_WIDTH // 8

# Tạo font
medium_font = pygame.font.SysFont('roboto', 20)
large_font = pygame.font.SysFont('roboto', 40)

# Tạo bàn cờ
def draw_board():
    '''for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))'''

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, '#ebecd0', [i * 100, j * 100, 100, 100])
            else:
                pygame.draw.rect(screen, '#739552', [i * 100, j * 100, 100, 100])
        # Vẽ chữ hàng
        for i in range(8):
            text = medium_font.render(chr(ord('A') + i), True, 'black')
            screen.blit(text, (15 + i * 100 + 100 // 3, 790))

        # Vẽ chữ cột
        for i in range(8):
            text = medium_font.render(str(8 - i), True, 'black')
            screen.blit(text, (790, 10 + i * 100 + 100 // 3))
# Tải hình ảnh quân cờ
def load_pieces():
    pieces = {}
    pieces['P'] = pygame.transform.scale(pygame.image.load('assets/images/white_pawn.png'), PIECE_SIZE)
    pieces['R'] = pygame.transform.scale(pygame.image.load('assets/images/white_rook.png'), PIECE_SIZE)
    pieces['N'] = pygame.transform.scale(pygame.image.load('assets/images/white_knight.png'), PIECE_SIZE)
    pieces['B'] = pygame.transform.scale(pygame.image.load('assets/images/white_bishop.png'), PIECE_SIZE)
    pieces['Q'] = pygame.transform.scale(pygame.image.load('assets/images/white_queen.png'), PIECE_SIZE)
    pieces['K'] = pygame.transform.scale(pygame.image.load('assets/images/white_king.png'), PIECE_SIZE)
    pieces['p'] = pygame.transform.scale(pygame.image.load('assets/images/black_pawn.png'), PIECE_SIZE)
    pieces['r'] = pygame.transform.scale(pygame.image.load('assets/images/black_rook.png'), PIECE_SIZE)
    pieces['n'] = pygame.transform.scale(pygame.image.load('assets/images/black_knight.png'), PIECE_SIZE)
    pieces['b'] = pygame.transform.scale(pygame.image.load('assets/images/black_bishop.png'), PIECE_SIZE)
    pieces['q'] = pygame.transform.scale(pygame.image.load('assets/images/black_queen.png'), PIECE_SIZE)
    pieces['k'] = pygame.transform.scale(pygame.image.load('assets/images/black_king.png'), PIECE_SIZE)
    return pieces



# Hiển thị các quân cờ trên bàn cờ
def draw_pieces(board, pieces):
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, row))
            if piece:
                screen.blit(pieces[piece.symbol()], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

selected_square = None

def draw_valid_moves(board, square):
    # Lấy tất cả các nước đi hợp lệ của quân cờ tại vị trí được chọn
    valid_moves = [move for move in board.legal_moves if move.from_square == square]

    # Vẽ các vòng tròn tại các ô vuông mà quân cờ có thể di chuyển tới
    for move in valid_moves:
        to_square = move.to_square
        row, col = chess.square_rank(to_square), chess.square_file(to_square)
        pygame.draw.circle(screen, (0, 255, 0),
                           (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                           SQUARE_SIZE // 6)

def handle_click(board, col, row):
    global selected_square
    square = chess.square(col, row)
    if selected_square is None:
        if board.piece_at(square):
            selected_square = square
    else:
        move = chess.Move(selected_square, square)
        if move in board.legal_moves:
            board.push(move)
        selected_square = None

def main():
    board = chess.Board()
    pieces = load_pieces()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE
                handle_click(board, col, row)

        draw_board()
        draw_pieces(board, pieces)

        if selected_square is not None:
            draw_valid_moves(board, selected_square)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
