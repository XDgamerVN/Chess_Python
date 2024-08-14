import pygame
from constants import *
from board import *
from pieces.queen import check_queen
from pieces.bishop import check_bishop
from pieces.knight import check_knight
from pieces.rook import check_rook

pygame.init()


# vẽ các quân cờ lên bảng
def draw_pieces():
    # Draw white pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100, white_locations[i][1] * 100))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                  100, 100], 5)

    # Draw black pieces
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100, black_locations[i][1] * 100))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 5)

# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    global castling_moves
    moves_list = []
    all_moves_list = []
    castling_moves = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list, castling_moves = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check king valid moves
def check_king(position, color):
    """
    Hàm kiểm tra các nước đi hợp lệ của quân vua dựa trên vị trí hiện tại và màu sắc,
    bao gồm cả các nước nhập thành.

    Parameters:
    - position: tuple chứa tọa độ hiện tại của quân vua (x, y).
    - color: chuỗi 'white' hoặc 'black' để xác định màu của quân vua.

    Returns:
    - moves_list: danh sách các tọa độ mà quân vua có thể di chuyển đến.
    - castle_moves: danh sách các nước nhập thành hợp lệ.
    """
    moves_list = []
    castle_moves = check_castling()  # Kiểm tra các nước nhập thành hợp lệ

    # Xác định danh sách quân đồng minh dựa trên màu sắc của quân vua
    friends_list = white_locations if color == 'white' else black_locations

    # Các nước đi hợp lệ cho vua: vua có thể di chuyển một ô theo bất kỳ hướng nào
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]

    for dx, dy in targets:
        target = (position[0] + dx, position[1] + dy)
        # Kiểm tra xem vị trí di chuyển có nằm trong giới hạn bàn cờ và không có quân đồng minh
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list, castle_moves


# check valid pawn moves
def check_pawn(position, color):
    """
    Hàm kiểm tra các nước đi hợp lệ của quân tốt dựa trên vị trí hiện tại và màu sắc.

    Parameters:
    - position: tuple chứa tọa độ hiện tại của quân tốt (x, y).
    - color: chuỗi 'white' hoặc 'black' để xác định màu của quân tốt.

    Returns:
    - moves_list: danh sách các tọa độ mà quân tốt có thể di chuyển đến.
    """
    moves_list = []
    direction = 1 if color == 'white' else -1  # Xác định hướng di chuyển dựa trên màu sắc (trắng đi lên, đen đi xuống)
    start_row = 1 if color == 'white' else 6  # Hàng khởi đầu của tốt (trắng ở hàng 1, đen ở hàng 6)
    enemies_list = black_locations if color == 'white' else white_locations  # Danh sách quân địch
    friends_list = white_locations if color == 'white' else black_locations  # Danh sách quân cùng màu
    ep_target = black_ep if color == 'white' else white_ep  # Mục tiêu bắt tốt qua đường (en passant)

    # Kiểm tra di chuyển một ô về phía trước
    forward_one = (position[0], position[1] + direction)
    if forward_one not in friends_list and forward_one not in enemies_list and 0 <= forward_one[1] <= 7:
        moves_list.append(forward_one)

        # Kiểm tra di chuyển hai ô về phía trước từ vị trí khởi đầu
        if position[1] == start_row:
            forward_two = (position[0], position[1] + 2 * direction)
            if forward_two not in friends_list and forward_two not in enemies_list:
                moves_list.append(forward_two)

    # Kiểm tra ăn quân địch chéo sang trái và phải
    for dx in [-1, 1]:
        diagonal = (position[0] + dx, position[1] + direction)
        if diagonal in enemies_list or diagonal == ep_target:  # Kiểm tra bắt qua đường (en passant)
            moves_list.append(diagonal)

    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    for i in range(len(moves)):
        pygame.draw.circle(screen, 'blue', (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))


# draw a flashing square around king if in check
def draw_check():
    """
    Hàm kiểm tra xem vua có đang bị chiếu (check) hay không và vẽ khung xung quanh vua nếu bị chiếu.

    Các biến toàn cục:
    - check: cờ đánh dấu trạng thái chiếu.
    - turn_step: bước đi hiện tại trong trò chơi (dùng để xác định lượt đi của trắng hoặc đen).
    - white_pieces, black_pieces: danh sách các quân cờ trắng và đen.
    - white_locations, black_locations: vị trí của các quân cờ trắng và đen.
    - white_options, black_options: các nước đi có thể của quân trắng và đen.
    - screen: màn hình trò chơi.
    - counter: biến đếm để tạo hiệu ứng nhấp nháy khi bị chiếu.
    """
    global check
    check = False  # Đặt lại cờ check trước mỗi lần kiểm tra

    if turn_step < 2:  # Lượt đi của quân trắng
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]

            # Kiểm tra nếu vua trắng bị chiếu
            for options in black_options:
                if king_location in options:
                    check = True
                    if counter < 15:  # Tạo hiệu ứng nhấp nháy trong 15 lần đầu
                        pygame.draw.rect(screen, 'red', [king_location[0] * 100 + 1,
                                                              king_location[1] * 100 + 1, 100, 100], 5)
    else:  # Lượt đi của quân đen
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]

            # Kiểm tra nếu vua đen bị chiếu
            for options in white_options:
                if king_location in options:
                    check = True
                    if counter < 15:  # Tạo hiệu ứng nhấp nháy trong 15 lần đầu
                        pygame.draw.rect(screen, 'red', [king_location[0] * 100 + 1,
                                                               king_location[1] * 100 + 1, 100, 100], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


# check en passant because people on the internet won't stop bugging me for it
def check_ep(old_coords, new_coords):
    if turn_step <= 1:
        index = white_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] - 1)
        piece = white_pieces[index]
    else:
        index = black_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] + 1)
        piece = black_pieces[index]
    if piece == 'pawn' and abs(old_coords[1] - new_coords[1]) > 1:
        # if piece was pawn and moved two spaces, return EP coords as defined above
        pass
    else:
        ep_coords = (100, 100)
    return ep_coords


# add castling
def check_castling():
    # king must not currently be in check, neither the rook nor king has moved previously, nothing between
    # and the king does not pass through or finish on an attacked piece
    castle_moves = []  # store each valid castle move as [((king_coords), (castle_coords))]
    rook_indexes = []
    rook_locations = []
    king_index = 0
    king_pos = (0, 0)
    if turn_step > 1:
        for i in range(len(white_pieces)):
            if white_pieces[i] == 'rook':
                rook_indexes.append(white_moved[i])
                rook_locations.append(white_locations[i])
            if white_pieces[i] == 'king':
                king_index = i
                king_pos = white_locations[i]
        if not white_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]),
                                     (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]),
                                     (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in white_locations or empty_squares[j] in black_locations or \
                            empty_squares[j] in black_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    else:
        for i in range(len(black_pieces)):
            if black_pieces[i] == 'rook':
                rook_indexes.append(black_moved[i])
                rook_locations.append(black_locations[i])
            if black_pieces[i] == 'king':
                king_index = i
                king_pos = black_locations[i]
        if not black_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]),
                                     (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]),
                                     (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in white_locations or empty_squares[j] in black_locations or \
                            empty_squares[j] in white_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    return castle_moves


def draw_castling(moves):
    for i in range(len(moves)):
        pygame.draw.circle(screen, 'red', (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70), 8)
        screen.blit(font.render('king', True, 'black'), (moves[i][0][0] * 100 + 30, moves[i][0][1] * 100 + 70))
        pygame.draw.circle(screen, 'red', (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 8)
        screen.blit(font.render('rook', True, 'black'),
                    (moves[i][1][0] * 100 + 30, moves[i][1][1] * 100 + 70))
        pygame.draw.line(screen, 'red', (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70),
                         (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 2)


# add pawn promotion
def check_promotion():
    pawn_indexes = []
    white_promotion = False
    black_promotion = False
    promote_index = 100
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if white_locations[pawn_indexes[i]][1] == 7:
            white_promotion = True
            promote_index = pawn_indexes[i]
    pawn_indexes = []
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if black_locations[pawn_indexes[i]][1] == 0:
            black_promotion = True
            promote_index = pawn_indexes[i]
    return white_promotion, black_promotion, promote_index


def draw_promotion():
    pygame.draw.rect(screen, 'dark gray', [800, 0, 200, 420])
    if white_promote:
        color = 'white'
        for i in range(len(white_promotions)):
            piece = white_promotions[i]
            index = piece_list.index(piece)
            screen.blit(white_images[index], (860, 5 + 100 * i))
    elif black_promote:
        color = 'black'
        for i in range(len(black_promotions)):
            piece = black_promotions[i]
            index = piece_list.index(piece)
            screen.blit(black_images[index], (860, 5 + 100 * i))
    pygame.draw.rect(screen, color, [800, 0, 200, 420], 8)


def check_promo_select():
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x_pos = mouse_pos[0] // 100
    y_pos = mouse_pos[1] // 100
    if white_promote and left_click and x_pos > 7 and y_pos < 4:
        white_pieces[promo_index] = white_promotions[y_pos]
    elif black_promote and left_click and x_pos > 7 and y_pos < 4:
        black_pieces[promo_index] = black_promotions[y_pos]

# Draw yellow rectangles for old and new positions (only once)
def draw_move_indicator(old_pos, new_pos):
    if old_pos is not None and is_valid_position(old_pos):
        pygame.draw.rect(screen, 'yellow', [old_pos[0] * 100, old_pos[1] * 100, 100, 100], 5)
    if new_pos is not None and is_valid_position(new_pos):
        pygame.draw.rect(screen, 'yellow', [new_pos[0] * 100, new_pos[1] * 100, 100, 100], 5)


def is_valid_position(pos):
    if len(pos) != 2:
        return False
    x_coord, y_coord = pos
    return 0 <= x_coord < 8 and 0 <= y_coord < 8


# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
old_pos = None
new_pos = None
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_move_indicator(old_pos, new_pos)
    draw_captured()
    draw_check()

    if not game_over:
        white_promote, black_promote, promo_index = check_promotion()
        if white_promote or black_promote:
            draw_promotion()
            check_promo_select()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
        if selected_piece == 'king':
            draw_castling(castling_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)

            if is_valid_position((x_coord, y_coord)):
                if selection is not None:
                    new_pos = (x_coord, y_coord)
                    if 'selected_piece' not in locals():
                        selected_piece = None
                    if selected_piece and (new_pos != old_pos):
                        # Update position of the selected piece
                        if turn_step < 2:
                            index = selection
                            if index < len(white_promotions):
                                white_locations[index] = new_pos
                            else:
                                print("Error: Index out of range")
                                black_locations[index] = new_pos
                        else:
                            index = selection
                            if index < len(black_locations):
                                black_locations[index] = new_pos
                            else:
                                print("Error: Index out of range")
                        old_pos = selected_piece
                        selection = None
                        selected_piece = None
                else:
                    # Select a piece
                    if turn_step < 2 and (x_coord, y_coord) in white_locations:
                        selection = white_locations.index((x_coord, y_coord))
                        selected_piece = (x_coord, y_coord)
                    elif turn_step >= 2 and (x_coord, y_coord) in black_locations:
                        selection = black_locations.index((x_coord, y_coord))
                        selected_piece = (x_coord, y_coord)
                    old_pos = None

                # Update valid moves and handle selection
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    # check what piece is selected, so you can only draw castling moves if king is selected
                    selected_piece = white_pieces[selection]
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_ep = check_ep(white_locations[selection], click_coords)
                    white_locations[selection] = click_coords
                    white_moved[selection] = True
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        black_moved.pop(black_piece)
                    # adding check if en passant pawn was captured
                    if click_coords == black_ep:
                        black_piece = black_locations.index((black_ep[0], black_ep[1] - 1))
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        black_moved.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                # add option to castle
                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        # check if the click is in the castling moves
                        if q < len(castling_moves) and click_coords == castling_moves[q][0]:
                            white_locations[selection] = click_coords
                            white_moved[selection] = True
                            if click_coords == (1, 0):
                                rook_coords = (0, 0)
                            else:
                                rook_coords = (7, 0)
                            rook_index = white_locations.index(rook_coords)
                            white_locations[rook_index] = castling_moves[q][1]
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 2
                            selection = 100
                            valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    # check what piece is selected, so you can only draw castling moves if king is selected
                    selected_piece = black_pieces[selection]
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_ep = check_ep(black_locations[selection], click_coords)
                    black_locations[selection] = click_coords
                    black_moved[selection] = True
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        white_moved.pop(white_piece)
                    if click_coords == white_ep:
                        white_piece = white_locations.index((white_ep[0], white_ep[1] + 1))
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        white_moved.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                # add option to castle
                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        # check if the click is in the castling moves
                        if q < len(castling_moves) and click_coords == castling_moves[q][0]:
                            # check if the click is in the castling moves
                            black_locations[selection] = click_coords
                            black_moved[selection] = True
                            if click_coords == (1, 7):
                                rook_coords = (0, 7)
                            else:
                                rook_coords = (7, 7)
                            rook_index = black_locations.index(rook_coords)
                            black_locations[rook_index] = castling_moves[q][1]
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 0
                            selection = 100
                            valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                white_moved = [False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                black_moved = [False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()