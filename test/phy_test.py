import pygame
import chess

# Khởi tạo Pygame
pygame.init()

# Chỉ cầm sửa duy nhất vị trí này để thay đổi toàn bộ tỉ lệ
CHESS_BOARD = 700

# Thiết lập kích thước màn hình
WIDTH = CHESS_BOARD * 1.5
HEIGHT = CHESS_BOARD * 1.17
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess by Dũng")

# Định nghĩa các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BAKCGROUND = (179, 172, 168)
YEllOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GRAYISH_YEllOW = (235, 236, 208)
MOSTLY_DESATURATED_DARK_GREEN = (115, 149, 82)

# Thiết lập kích thước ô vuông trên bàn cờ
SQUARE_SIZE = CHESS_BOARD // 8

# Thiết lập kích thước quân cờ và quân cờ nhỏ
PIECE_SIZE = (SQUARE_SIZE, SQUARE_SIZE)
CAPTURED_PIECE_SIZE = (SQUARE_SIZE // 1.75, SQUARE_SIZE // 1.75)

# Tạo font
FONT = 'jetbrains mono'
medium_font = pygame.font.SysFont(FONT, CHESS_BOARD//40)
large_font = pygame.font.SysFont(FONT, CHESS_BOARD//25)


# Tạo bàn cờ
def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_GRAYISH_YEllOW if (row + col) % 2 == 0 else MOSTLY_DESATURATED_DARK_GREEN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, BLACK, pygame.Rect(SQUARE_SIZE // 100, SQUARE_SIZE * 8.1,
                                                SQUARE_SIZE * 12, SQUARE_SIZE // 1.75), 1)
    pygame.draw.rect(screen, BLACK, pygame.Rect(SQUARE_SIZE // 100, SQUARE_SIZE * 8.7,
                                                SQUARE_SIZE * 12, SQUARE_SIZE // 1.75), 1)

    # Vẽ chữ hàng
    for i in range(8):
        color = LIGHT_GRAYISH_YEllOW if i % 2 == 0 else MOSTLY_DESATURATED_DARK_GREEN
        text = medium_font.render(chr(ord('a') + i), True, color)
        screen.blit(text, (SQUARE_SIZE * 0.87 + i * SQUARE_SIZE, SQUARE_SIZE * 7.74))

    # Vẽ chữ cột
    for i in range(8):
        color = MOSTLY_DESATURATED_DARK_GREEN if i % 2 == 0 else LIGHT_GRAYISH_YEllOW
        text = medium_font.render(str(8 - i), True, color)
        screen.blit(text, (SQUARE_SIZE * 0.022, i * SQUARE_SIZE))

    # Hiển thị tên người chơi
    text = large_font.render('Nguyễn Lê Văn Dũng', True, BLACK)
    screen.blit(text, (SQUARE_SIZE * 8.2, SQUARE_SIZE * 3))


# Tải hình ảnh quân cờ
def load_pieces():
    pieces = {'P': pygame.transform.scale(pygame.image.load('assets/pieces/white_pawn.png'), PIECE_SIZE),
              'R': pygame.transform.scale(pygame.image.load('assets/pieces/white_rook.png'), PIECE_SIZE),
              'N': pygame.transform.scale(pygame.image.load('assets/pieces/white_knight.png'), PIECE_SIZE),
              'B': pygame.transform.scale(pygame.image.load('assets/pieces/white_bishop.png'), PIECE_SIZE),
              'Q': pygame.transform.scale(pygame.image.load('assets/pieces/white_queen.png'), PIECE_SIZE),
              'K': pygame.transform.scale(pygame.image.load('assets/pieces/white_king.png'), PIECE_SIZE),
              'p': pygame.transform.scale(pygame.image.load('assets/pieces/black_pawn.png'), PIECE_SIZE),
              'r': pygame.transform.scale(pygame.image.load('assets/pieces/black_rook.png'), PIECE_SIZE),
              'n': pygame.transform.scale(pygame.image.load('assets/pieces/black_knight.png'), PIECE_SIZE),
              'b': pygame.transform.scale(pygame.image.load('assets/pieces/black_bishop.png'), PIECE_SIZE),
              'q': pygame.transform.scale(pygame.image.load('assets/pieces/black_queen.png'), PIECE_SIZE),
              'k': pygame.transform.scale(pygame.image.load('assets/pieces/black_king.png'), PIECE_SIZE)}

    captured_pieces = {'P': pygame.transform.scale(pygame.image.load('assets/pieces/white_pawn.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'R': pygame.transform.scale(pygame.image.load('assets/pieces/white_rook.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'N': pygame.transform.scale(pygame.image.load('assets/pieces/white_knight.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'B': pygame.transform.scale(pygame.image.load('assets/pieces/white_bishop.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'Q': pygame.transform.scale(pygame.image.load('assets/pieces/white_queen.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'K': pygame.transform.scale(pygame.image.load('assets/pieces/white_king.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'p': pygame.transform.scale(pygame.image.load('assets/pieces/black_pawn.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'r': pygame.transform.scale(pygame.image.load('assets/pieces/black_rook.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'n': pygame.transform.scale(pygame.image.load('assets/pieces/black_knight.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'b': pygame.transform.scale(pygame.image.load('assets/pieces/black_bishop.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'q': pygame.transform.scale(pygame.image.load('assets/pieces/black_queen.png'),
                                                    CAPTURED_PIECE_SIZE),
                       'k': pygame.transform.scale(pygame.image.load('assets/pieces/black_king.png'),
                                                    CAPTURED_PIECE_SIZE)}
    return pieces, captured_pieces


# Hiển thị các quân cờ trên bàn cờ
def draw_pieces(board, pieces, selected_square=None):
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)  # Đảo ngược thứ tự hàng
            if piece:
                if selected_square == square:
                    # Vẽ viền xanh lá quanh quân cờ được chọn
                    pygame.draw.rect(screen, BLUE, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE,
                                                                SQUARE_SIZE, SQUARE_SIZE), 4)
                screen.blit(pieces[piece.symbol()], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE,
                                                                SQUARE_SIZE, SQUARE_SIZE))


# Hiển thị quân cờ bị ăn
def draw_captured_pieces(captured_pieces_list, captured_pieces):
    white_offset = 0
    black_offset = 0
    for piece in captured_pieces_list:
        if piece.isupper():  # Quân trắng
            screen.blit(captured_pieces[piece], (SQUARE_SIZE // 100 + white_offset, SQUARE_SIZE * 8.1))
            white_offset += CAPTURED_PIECE_SIZE[0] + 5
        else:  # Quân đen
            screen.blit(captured_pieces[piece], (SQUARE_SIZE // 100 + black_offset, SQUARE_SIZE * 8.7))
            black_offset += CAPTURED_PIECE_SIZE[0] + 5


selected_square = None
captured_pieces_list = []
previous_move = None


# Hiển thị các nước đi hợp lệ
def draw_valid_moves(board, square):
    valid_moves = [move for move in board.legal_moves if move.from_square == square]
    for move in valid_moves:
        to_square = move.to_square
        row, col = chess.square_rank(to_square), chess.square_file(to_square)
        pygame.draw.circle(screen, BLUE,
                           (col * SQUARE_SIZE + SQUARE_SIZE // 2, (7 - row) * SQUARE_SIZE + SQUARE_SIZE // 2),
                           SQUARE_SIZE // 6)


# Hiển thị ô vuông màu đỏ khi vua bị chiếu
def draw_check_square(board):
    if board.is_check():
        king_square = board.king(board.turn)
        row, col = chess.square_rank(king_square), chess.square_file(king_square)
        pygame.draw.rect(screen, RED,
                         pygame.Rect(col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),4)


# Hiển thị ô vuông vàng ở vị trí trước và sau khi di chuyển
def draw_previous_move(previous_move):
    if previous_move:
        from_square = previous_move.from_square
        to_square = previous_move.to_square
        from_row, from_col = chess.square_rank(from_square), chess.square_file(from_square)
        to_row, to_col = chess.square_rank(to_square), chess.square_file(to_square)
        pygame.draw.rect(screen, YEllOW, pygame.Rect(from_col * SQUARE_SIZE, (7 - from_row) * SQUARE_SIZE,
                                                        SQUARE_SIZE, SQUARE_SIZE), 4)
        pygame.draw.rect(screen, YEllOW, pygame.Rect(to_col * SQUARE_SIZE, (7 - to_row) * SQUARE_SIZE,
                                                        SQUARE_SIZE, SQUARE_SIZE), 4)


# Xử lý sự kiện khi người chơi click chuột
def handle_click(board, col, row):
    global selected_square, previous_move

    square = chess.square(col, row)
    piece = board.piece_at(square)

    if selected_square is None:
        if piece is not None and piece.color == board.turn:
            selected_square = square
    else:
        move = chess.Move(selected_square, square)
        if move in board.legal_moves:
            captured_piece = board.piece_at(square)

            # Kiểm tra nếu nước đi là bắt tốt qua đường
            if board.is_en_passant(move):
                # Xác định vị trí của quân tốt bị bắt
                en_passant_capture_square = chess.square(col, chess.square_rank(selected_square))
                captured_piece = board.piece_at(en_passant_capture_square)
                if captured_piece:
                    captured_pieces_list.append(captured_piece.symbol())

            elif captured_piece:  # Kiểm tra nếu có quân cờ bị ăn
                captured_pieces_list.append(captured_piece.symbol())

            board.push(move)
            selected_square = None
            previous_move = move

            # Xử lý phong cấp
            if board.is_checkmate():
                print("Checkmate!")
            elif board.is_stalemate():
                print("Stalemate!")
            if move.promotion:
                board.remove_piece_at(move.to_square)
                board.set_piece_at(move.to_square, chess.Piece(chess.QUEEN, board.turn))
        else:
            selected_square = None


def main():
    running = True
    clock = pygame.time.Clock()
    board = chess.Board()
    pieces, captured_pieces = load_pieces()

    while running:
        screen.fill(BAKCGROUND)
        draw_board()
        draw_previous_move(previous_move)
        draw_pieces(board, pieces, selected_square)
        draw_captured_pieces(captured_pieces_list, captured_pieces)
        draw_check_square(board)

        if selected_square is not None:
            draw_valid_moves(board, selected_square)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x < CHESS_BOARD and y < CHESS_BOARD:
                    col = x // SQUARE_SIZE
                    row = 7 - (y // SQUARE_SIZE)
                    handle_click(board, col, row)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
