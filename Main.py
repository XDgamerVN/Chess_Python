from Engine import *
from Constants import *
import pygame as p

p.init()

def draw_game_state(screen, game_state, square_selected):
    draw_board(screen)  # Vẽ bàn cờ
    highlight_squares(screen, game_state, square_selected)  # Làm nổi bật ô được chọn và các ô có thể đi được

    # Kiểm tra nếu quân vua bị chiếu và thêm viền đỏ
    if game_state.in_check:
        king_position = game_state.find_king(game_state.white_to_move)  # Lấy vị trí của vua
        highlight_king_in_check(screen, king_position) # Vẽ viền đỏ quanh vua

    draw_pieces(screen, game_state.board)  # Vẽ các quân cờ trên bàn cờ
    draw_captured_pieces(screen, game_state.captured_pieces)  # Vẽ các quân cờ đã bị ăn

    # Hiển thị các nước đi hợp lệ
    if square_selected != ():
        row, col = square_selected
        piece = game_state.board[row][col]
        if (piece[0] == 'w' and game_state.white_to_move) or (piece[0] == 'b' and not game_state.white_to_move):
            valid_moves = game_state.get_valid_moves()
            highlight_valid_moves(screen, game_state, valid_moves, square_selected)

    draw_move_log(screen, game_state)  # Vẽ lịch sử các nước đi

def draw_board(screen):
    """Draw squares on the board using a chess.com colouring pattern"""
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            colour = COLOR_A[((row + column) % 2)]
            p.draw.rect(screen, colour, p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    # Vẽ chữ hàng
    for i in range(DIMENSION):
        color = COLOR_A[(i % 2)]
        text = medium_font.render(chr(ord('a') + i), True, color)
        screen.blit(text, (SQ_SIZE * 0.86 + i * SQ_SIZE, SQ_SIZE * 7.7))
    # Vẽ chữ cột
    for i in range(DIMENSION):
        color = COLOR_Z[(i % 2)]
        text = medium_font.render(str(8 - i), True, color)
        screen.blit(text, (SQ_SIZE * 0.05, SQ_SIZE // 25 + i * SQ_SIZE))
    p.draw.rect(screen, 'grey22', p.Rect(0, SQ_SIZE * 8.2, SQ_SIZE * 8, SQ_SIZE // 1.75), 2)
    p.draw.rect(screen, 'grey22', p.Rect(0, SQ_SIZE * 8.8, SQ_SIZE * 8, SQ_SIZE // 1.75), 2)

def draw_pieces(screen, board):
    """Draws pieces on the board using the current GameState.board"""
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != '--':  # Add pieces if not an empty square
                screen.blit(images[piece], p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_captured_pieces(screen, captured_pieces):
    """Vẽ các quân cờ đã bị ăn theo hàng ngang, quân trắng nằm trên, quân đen nằm dưới"""
    white_captures = [p for p in captured_pieces if p[0] == 'w']
    black_captures = [p for p in captured_pieces if p[0] == 'b']

    # Vẽ quân cờ trắng đã bị ăn (hàng trên)
    for i, piece in enumerate(white_captures):
        piece_image = captures_images.get(piece)
        if piece_image:
            screen.blit(piece_image, (i * SQ_SIZE // 2, SQ_SIZE * 8.2))

    # Vẽ quân cờ đen đã bị ăn (hàng dưới)
    for i, piece in enumerate(black_captures):
        piece_image = captures_images.get(piece)
        if piece_image:
            screen.blit(piece_image, (i * SQ_SIZE // 2, SQ_SIZE * 8.8))

def highlight_king_in_check(screen, king_position):
    """Hàm vẽ viền đỏ quanh quân vua khi bị chiếu"""
    row, col = king_position
    highlight_king = p.Surface((SQ_SIZE, SQ_SIZE))
    highlight_king.set_alpha(100)  # Độ trong suốt
    highlight_king.fill(p.Color('red'))  # Màu đỏ
    screen.blit(highlight_king, (col * SQ_SIZE, row * SQ_SIZE))

def highlight_squares(screen, game_state, square_selected):
    """Highlights square selected and last move made"""
    # Highlights selected square
    if square_selected != ():
        row, column = square_selected
        if game_state.board[row][column][0] == ('w' if game_state.white_to_move else 'b'):  # Clicks on own piece
            highlight_selected = p.Surface((SQ_SIZE, SQ_SIZE))
            highlight_selected.set_alpha(70)  # Transperancy value; 0 transparent; 255 opaque
            highlight_selected.fill(p.Color('blue'))
            screen.blit(highlight_selected, (column * SQ_SIZE, row * SQ_SIZE))

    # Highlights last move
    if len(game_state.move_log) != 0:
        last_move = game_state.move_log[-1]
        start_row, start_column = last_move.start_row, last_move.start_column
        end_row, end_column = last_move.end_row, last_move.end_column
        highlight_last = p.Surface((SQ_SIZE, SQ_SIZE))
        highlight_last.set_alpha(70)
        highlight_last.fill(p.Color('yellow'))
        screen.blit(highlight_last, (start_column * SQ_SIZE, start_row * SQ_SIZE))
        screen.blit(highlight_last, (end_column * SQ_SIZE, end_row * SQ_SIZE))

def highlight_valid_moves(screen, game_state, valid_moves, square_selected):
    """Vẽ các nước đi hợp lệ khi người chơi chọn một quân cờ"""
    for move in valid_moves:
        if move.start_row == square_selected[0] and move.start_column == square_selected[1]:
            highlight_moves = p.Surface((SQ_SIZE, SQ_SIZE), p.SRCALPHA)
            highlight_moves.set_alpha(100)  # Độ trong suốt
            p.draw.circle(highlight_moves, 'blue', (SQ_SIZE // 2, SQ_SIZE // 2), SQ_SIZE // 6)
            screen.blit(highlight_moves, (move.end_column * SQ_SIZE, move.end_row * SQ_SIZE))

def draw_move_log(screen, game_state):
    """Draws move log to the right of the screen"""
    move_log_area = p.Rect(SQ_SIZE * 8, SQ_SIZE * 3, SQ_SIZE * 5, SQ_SIZE * 5)
    p.draw.rect(screen, p.Color('grey22'), move_log_area)
    move_log = game_state.move_log
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = f'{i // 2 + 1}. {str(move_log[i])} '
        if i + 1 < len(move_log):  # Makes sure black has made a move
            move_string += f'{str(move_log[i + 1])} '
        move_texts.append(move_string)

    move_padding = 4
    text_y = move_padding
    for j in range(0, len(move_texts), 4):
        text_line = ' | '.join(move_texts[j:j + 4])  # Ghi lại 5 lượt đi chung trên 1 dòng
        text_object = small_font.render(text_line, True, p.Color('white'))
        text_location = move_log_area.move(move_padding, text_y)
        screen.blit(text_object, text_location)
        text_y += text_object.get_height()

def animate_move(move, screen, board, clock):
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

        # Erases the piece from its ending square
        colour = COLOR_A[(move.end_row + move.end_column) % 2]
        end_square = p.Rect(move.end_column * SQ_SIZE, move.end_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, colour, end_square)

        # Draws a captured piece onto the rectangle if a piece is captured
        if move.piece_captured != '--':
            if move.is_en_passant_move:
                en_passant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = p.Rect(move.end_column * SQ_SIZE, en_passant_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            screen.blit(images[move.piece_captured], end_square)

        # Draws moving piece
        screen.blit(images[move.piece_moved], p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

        p.display.flip()
        clock.tick(60)  # Controls fame rate per second for the animation

def draw_endgame_text(screen, text):
    """Vẽ văn bản khi kết thúc trò chơi"""
    text_object = large_font.render(text, True, p.Color('gray'), p.Color('mintcream'))
    text_location = p.Rect(0, 0, WIDTH, HEIGHT).move(SQ_SIZE * 8 - text_object.get_width() / 2,
                                                     SQ_SIZE * 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)

    # Creates a shadowing effect
    text_object = large_font.render(text, True, p.Color('black'))
    screen.blit(text_object, text_location.move(2, 2))

def main():
    """Main function which handles user input and updates graphics"""
    clock = p.time.Clock()
    screen.fill(p.Color('dark grey'))
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
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

            # Mouse handler
            elif event.type == p.MOUSEBUTTONDOWN:
                if not game_over:
                    location = p.mouse.get_pos()  # (x, y) location of mouse
                    column = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if square_selected == (row, column) or column >= DIMENSION:  # User clicks same square or move log
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
            elif event.type == p.KEYDOWN:
                if event.key == p.K_z:  # Undo move when 'z' is pressed
                    game_state.undo_move()
                    move_made = True
                    animate = False
                    game_over = False
                if event.key == p.K_r:  # Reset board when 'r' is pressed
                    game_state = GameState()
                    valid_moves = game_state.get_valid_moves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    game_over = False

        if move_made:
            if animate:
                animate_move(game_state.move_log[-1], screen, game_state.board, clock)
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
        p.display.flip()

if __name__ == '__main__':
    main()
