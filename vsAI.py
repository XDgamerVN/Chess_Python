from EngineAI import *
from ChessAI import *
from Constants import *
import pygame

pygame.init()

def version():
    version_font = pygame.font.SysFont('Arial', SQ_SIZE // 6, False, False)
    text_version = version_font.render('v0.4 beta', True, pygame.Color('white'))
    screen.blit(text_version, (SQ_SIZE * 13.4, SQ_SIZE * 7.6))

def draw_game_state(screen, game_state, square_selected):
    draw_board(screen)  # Vẽ bàn cờ
    highlight_squares(screen, game_state, square_selected)  # Làm nổi bật ô được chọn và các ô có thể đi được

    # Kiểm tra nếu quân vua bị chiếu và thêm viền đỏ
    if game_state.in_check:
        king_position = game_state.find_king(game_state.white_to_move)  # Lấy vị trí của vua
        highlight_king_in_check(screen, king_position) # Vẽ viền đỏ quanh vua

    draw_pieces(screen, game_state.board)  # Vẽ các quân cờ trên bàn cờ
    draw_captured_pieces(screen, game_state.white_captured_pieces, game_state.black_captured_pieces)

    # Hiển thị các nước đi hợp lệ
    if square_selected != ():
        row, col = square_selected
        piece = game_state.board[row][col]
        if (piece[0] == 'w' and game_state.white_to_move) or (piece[0] == 'b' and not game_state.white_to_move):
            valid_moves = game_state.get_valid_moves()
            highlight_valid_moves(screen, game_state, valid_moves, square_selected)

    draw_move_log(screen, game_state)  # Vẽ lịch sử các nước đi
    draw_turn_message(screen, game_state)  # Vẽ thông báo lượt chơi

def draw_board(screen):
    """Draw squares on the board using a chess.com colouring pattern"""
    for row in range(8):
        for column in range(8):
            colour = COLOR_A[((row + column) % 2)]
            pygame.draw.rect(screen, colour, pygame.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    # Vẽ chữ hàng
    for i in range(8):
        color = COLOR_A[(i % 2)]
        text = medium_font.render(chr(ord('a') + i), True, color)
        screen.blit(text, (SQ_SIZE * 0.86 + i * SQ_SIZE, SQ_SIZE * 7.7))
    # Vẽ chữ cột
    for i in range(8):
        color = COLOR_Z[(i % 2)]
        text = medium_font.render(str(8 - i), True, color)
        screen.blit(text, (SQ_SIZE * 0.05, SQ_SIZE // 25 + i * SQ_SIZE))
    #draw captured pieces
    pygame.draw.rect(screen, 'dark grey', pygame.Rect(SQ_SIZE * 8, SQ_SIZE * 2, SQ_SIZE * 2, SQ_SIZE * 7))
    pygame.draw.rect(screen, 'grey22', pygame.Rect(SQ_SIZE * 8.05, SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE * 6), 2)
    pygame.draw.rect(screen, 'grey22', pygame.Rect(SQ_SIZE * 8.65, SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE * 6), 2)
    # draw endgame text
    pygame.draw.rect(screen, 'grey22', pygame.Rect(SQ_SIZE * 8.05, 0, SQ_SIZE * 6.1, SQ_SIZE))
    # draw move log
    pygame.draw.rect(screen, pygame.Color('grey22'), pygame.Rect(SQ_SIZE * 9.25, SQ_SIZE * 2, SQ_SIZE * 4.9, SQ_SIZE * 7))
    version()


def draw_pieces(screen, board):
    """Draws pieces on the board using the current GameState.board. The board is an 8x8 2D list"""
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece != '--':  # Add pieces if not an empty square
                screen.blit(images[piece], pygame.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_captured_pieces(screen, white_captured_pieces, black_captured_pieces):
    """Vẽ các quân cờ đã bị ăn"""
    # Vẽ quân cờ trắng đã bị ăn
    for i, piece in enumerate(white_captured_pieces):
        piece_image = captures_images.get(piece)
        if piece_image:
            screen.blit(piece_image, (SQ_SIZE * 8.1, SQ_SIZE * 2 + i * SQ_SIZE // 2.6))

    # Vẽ quân cờ đen đã bị ăn
    for i, piece in enumerate(black_captured_pieces):
        piece_image = captures_images.get(piece)
        if piece_image:
            screen.blit(piece_image, (SQ_SIZE * 8.7, SQ_SIZE * 2 + i * SQ_SIZE // 2.6))

def highlight_king_in_check(screen, king_position):
    """Hàm vẽ viền đỏ quanh quân vua khi bị chiếu"""
    row, col = king_position
    highlight_king = pygame.Surface((SQ_SIZE, SQ_SIZE))
    highlight_king.set_alpha(100)  # Độ trong suốt
    highlight_king.fill(pygame.Color('red'))  # Màu đỏ
    screen.blit(highlight_king, (col * SQ_SIZE, row * SQ_SIZE))

def highlight_squares(screen, game_state, square_selected):
    """Highlights square selected and last move made"""
    # Highlights selected square
    if square_selected != ():
        row, column = square_selected
        if game_state.board[row][column][0] == ('w' if game_state.white_to_move else 'b'):  # Clicks on own piece
            highlight_selected = pygame.Surface((SQ_SIZE, SQ_SIZE))
            highlight_selected.set_alpha(70)  # Transperancy value; 0 transparent; 255 opaque
            highlight_selected.fill(pygame.Color('blue'))
            screen.blit(highlight_selected, (column * SQ_SIZE, row * SQ_SIZE))

    # Highlights last move
    if len(game_state.move_log) != 0:
        last_move = game_state.move_log[-1]
        start_row, start_column = last_move.start_row, last_move.start_column
        end_row, end_column = last_move.end_row, last_move.end_column
        highlight_last = pygame.Surface((SQ_SIZE, SQ_SIZE))
        highlight_last.set_alpha(70)
        highlight_last.fill(pygame.Color('yellow'))
        screen.blit(highlight_last, (start_column * SQ_SIZE, start_row * SQ_SIZE))
        screen.blit(highlight_last, (end_column * SQ_SIZE, end_row * SQ_SIZE))

def highlight_valid_moves(screen, game_state, valid_moves, square_selected):
    """Vẽ các nước đi hợp lệ khi người chơi chọn một quân cờ"""
    for move in valid_moves:
        if move.start_row == square_selected[0] and move.start_column == square_selected[1]:
            highlight_moves = pygame.Surface((SQ_SIZE, SQ_SIZE), pygame.SRCALPHA)
            highlight_moves.set_alpha(100)  # Độ trong suốt
            pygame.draw.circle(highlight_moves, 'blue', (SQ_SIZE // 2, SQ_SIZE // 2), SQ_SIZE // 6)
            screen.blit(highlight_moves, (move.end_column * SQ_SIZE, move.end_row * SQ_SIZE))

def draw_move_log(screen, game_state):
    """Draws move log to the right of the screen"""
    move_log_area = pygame.Rect(SQ_SIZE * 9.25, SQ_SIZE * 2, SQ_SIZE * 4.9, SQ_SIZE * 7)

    move_log = game_state.move_log
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = f'{i // 2 + 1}. {str(move_log[i])} '
        if i + 1 < len(move_log):  # Makes sure black has made a move
            move_string += f'{str(move_log[i + 1])} '
        move_texts.append(move_string)

    move_padding = 5
    text_y = move_padding
    for j in range(0, len(move_texts), 5):
        text_line = ' | '.join(move_texts[j:j + 5])
        text_object = small_font.render(text_line, True, pygame.Color('white'))
        text_location = move_log_area.move(move_padding, text_y)
        screen.blit(text_object, text_location)
        text_y += text_object.get_height()

def draw_turn_message(screen, game_state):
    """Vẽ thông báo lượt chơi của mỗi bên quân"""
    if game_state.white_to_move:
        turn_text = "White's turn"
        turn_color = pygame.Color('white')
        background_color = pygame.Color('black')
    else:
        turn_text = "Black's turn"
        turn_color = pygame.Color('black')
        background_color = pygame.Color('white')
    # Tạo surface cho thông báo
    pygame.draw.rect(screen, background_color, pygame.Rect(SQ_SIZE * 8.1, SQ_SIZE * 0.15, SQ_SIZE * 1.7, SQ_SIZE // 1.5))
    pygame.draw.rect(screen, turn_color, pygame.Rect(SQ_SIZE * 8.1, SQ_SIZE * 0.15, SQ_SIZE * 1.7, SQ_SIZE // 1.5), 3)
    turn_message_surface = large_font.render(turn_text, True, turn_color)
    # Vẽ thông báo ở góc trên bên trái
    screen.blit(turn_message_surface, (SQ_SIZE * 8.25, SQ_SIZE * 0.28))

def animate_move(move, screen, board, clock, game_state):
    """Animates a move"""
    delta_row = move.end_row - move.start_row  # Change in row
    delta_column = move.end_column - move.start_column  # Change in column
    frames_per_square = 5  # Controls animation speed (frames to move one square)
    frame_count = (abs(delta_row) + abs(delta_column)) * frames_per_square

    for frame in range(frame_count + 1):  # Need +1 to complete the entire animation

        #  Frame/frame_count indicates how far along the action is
        row, column = (
            move.start_row + delta_row * frame / frame_count, move.start_column + delta_column * frame / frame_count)

        # Draw board and pieces for each frame of the animation
        draw_board(screen)
        draw_pieces(screen, board)
        draw_captured_pieces(screen, game_state.white_captured_pieces, game_state.black_captured_pieces)
        draw_move_log(screen, game_state)
        draw_turn_message(screen, game_state)  # Vẽ thông báo lượt chơi
        replay_button = draw_button('(r) Replay', SQ_SIZE * 8.1, SQ_SIZE + BUTTON_HEIGHT / 2,
                                    'light grey', 'light green', 'dark green')

        undo_button = draw_button('(u) Undo', SQ_SIZE * 10.15, SQ_SIZE + BUTTON_HEIGHT / 2,
                                  'light grey', 'yellow', 'orange')

        exit_button = draw_button('(esc) Exit', SQ_SIZE * 12.2, SQ_SIZE + BUTTON_HEIGHT / 2,
                                  'light grey', 'red', 'dark red')

        # Erases the piece from its ending square
        colour = COLOR_A[(move.end_row + move.end_column) % 2]
        end_square = pygame.Rect(move.end_column * SQ_SIZE, move.end_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(screen, colour, end_square)

        # Draws a captured piece onto the rectangle if a piece is captured
        if move.piece_captured != '--':
            if move.is_en_passant_move:
                en_passant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = pygame.Rect(move.end_column * SQ_SIZE, en_passant_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            screen.blit(images[move.piece_captured], end_square)

        # Draws moving piece
        screen.blit(images[move.piece_moved], pygame.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

        pygame.display.flip()
        clock.tick(60)  # Controls fame rate per second for the animation

def draw_button(text, x, y, color, hover_color, border_color, border_radius=15, border_width=5):
    """Vẽ nút bo góc với màu sắc, viền và vị trí đã chỉ định"""
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    button_color = hover_color if button_rect.collidepoint(mouse_pos) else color

    # Vẽ viền nút
    draw_rounded_rect(screen, button_rect, border_radius, border_color, border_width)

    # Vẽ hình chữ nhật bo góc chính
    rounded_rect(screen, button_rect, border_radius, button_color)

    # Vẽ văn bản lên nút
    text_surface = large_font.render(text, True, 'black')
    screen.blit(text_surface, text_surface.get_rect(center=button_rect.center))
    return button_rect


def rounded_rect(surface, rect, radius, color):
    """Vẽ hình chữ nhật bo góc"""
    pygame.draw.rect(surface, color, rect, border_radius=radius)


def draw_rounded_rect(surface, rect, radius, color, border_width):
    """Vẽ hình chữ nhật bo góc với viền"""
    # Tạo hình chữ nhật viền
    border_rect = rect.inflate(border_width, border_width)
    pygame.draw.rect(surface, color, border_rect, border_radius=radius)

def draw_endgame_text(screen, text):
    """Vẽ văn bản khi kết thúc trò chơi"""
    text_object = large_font.render(text, True, pygame.Color('white'))
    text_location = pygame.Rect(SQ_SIZE * 10.4, SQ_SIZE * 0.28, 0, 0)
    screen.blit(text_object, text_location)


def play_game_AI(AI):
    """Main function which handles user input and updates graphics"""
    clock = pygame.time.Clock()
    screen.fill('dark grey')
    game_state = GameState()
    valid_moves = game_state.get_valid_moves()
    move_made = False  # Flag variable for when a move is made
    animate = False  # Flag variable for when a move should be animated
    load_images()
    load_captured_images()
    running = True
    square_selected = ()  # Keeps track of the last click by user (tuple: (row, column))
    player_clicks = []  # Keeps track of player clicks (two tuples: ex. [(6, 4), (4, 4)])
    game_over = False

    while running:
        human_turn = (game_state.white_to_move and True) or (not game_state.white_to_move and AI)

        replay_button = draw_button('(r) Replay', SQ_SIZE * 8.1, SQ_SIZE + BUTTON_HEIGHT / 2,
                                    'light grey', 'light green', 'dark green')

        undo_button = draw_button('(u) Undo', SQ_SIZE * 10.15, SQ_SIZE + BUTTON_HEIGHT / 2,
                                    'light grey', 'khaki1', 'orange')

        exit_button = draw_button('(esc) Exit', SQ_SIZE * 12.2, SQ_SIZE + BUTTON_HEIGHT / 2,
                                  'light grey', 'tomato', 'dark red')
        # Menu buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Mouse handler
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.collidepoint(event.pos):
                    game_state = GameState()
                    valid_moves = game_state.get_valid_moves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    game_over = False

                elif undo_button.collidepoint(event.pos):
                    game_state.undo_move()
                    valid_moves = game_state.get_valid_moves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False

                elif exit_button.collidepoint(event.pos):
                    return
                if not game_over and human_turn:
                    location = pygame.mouse.get_pos()  # (x, y) location of mouse
                    column = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE

                    if square_selected == (row, column) or column >= 8:  # User clicks same square or move log
                        square_selected = ()  # Deselects
                        player_clicks = []  # Clears player clicks
                    else:
                        square_selected = (row, column)
                        player_clicks.append(square_selected)  # Appends both 1st and 2nd clicks
                    if len(player_clicks) == 2:
                        move = Move(player_clicks[0], player_clicks[1], game_state.board)
                        for i in range(len(valid_moves)):
                            if move == valid_moves[i]:
                                game_state.make_move(valid_moves[i])
                                move_made = True
                                animate = True
                                square_selected = ()  # Resets user clicks
                                player_clicks = []
                        if not move_made:
                            player_clicks = [square_selected]

            # Key handlers
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset board when 'r' is pressed
                    game_state = GameState()
                    valid_moves = game_state.get_valid_moves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    game_over = False
                elif event.key == pygame.K_u:  # Undo move when 'z' is pressed
                    game_state.undo_move()
                    move_made = True
                    animate = False
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    return

        # Tìm nước đi của AI
        if not game_over and not human_turn:
            AI_move = find_best_move(game_state, valid_moves)
            if AI_move is None:
                AI_move = find_random_move(valid_moves)
            game_state.make_move(AI_move)
            move_made = True
            animate = True

        if move_made:
            if animate:
                animate_move(game_state.move_log[-1], screen, game_state.board, clock, game_state)
            valid_moves = game_state.get_valid_moves()
            move_made = False
            animate = False

        draw_game_state(screen, game_state, square_selected)

        if game_state.checkmate or game_state.stalemate:
            game_over = True
            if game_state.stalemate:
                text = 'Stalemate'
            else:
                text = 'Black wins by checkmate' if game_state.white_to_move else 'White wins by checkmate'
            draw_endgame_text(screen, text)

        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()