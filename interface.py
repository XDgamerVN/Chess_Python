from additions import *
from engine import *
from system import *
from negamaxAI import *

pygame.init()
version = "v0.5"

def support(SQ_SIZE):
    """Hiển thị cửa sổ hỗ trợ"""
    in_support = True
    while in_support:
        # Vẽ giao diện hỗ trợ tại đây
        draw_button("", 0, SQ_SIZE * 3, SQ_SIZE,
                    SQ_SIZE * 8, SQ_SIZE * 5 - SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 15,
                    'white', 'white', COLOR_SCREEN, COLOR_SCREEN, 'aquamarine')

        draw_button("", 0, SQ_SIZE * 8 + SQ_SIZE // 4, SQ_SIZE + SQ_SIZE // 4,
                    SQ_SIZE * 2 + SQ_SIZE // 2, SQ_SIZE * 4, SQ_SIZE // 7, SQ_SIZE // 22,
                    'white', 'white', COLOR_SCREEN, COLOR_SCREEN, 'grey')

        draw_button("", 0, SQ_SIZE * 3 + SQ_SIZE // 4, SQ_SIZE + SQ_SIZE // 4,
                    SQ_SIZE * 5 - SQ_SIZE // 4, SQ_SIZE * 4, SQ_SIZE // 7, SQ_SIZE // 22,
                    'white', 'white', COLOR_SCREEN, COLOR_SCREEN, 'grey')

        # Tạo font chữ
        font_support  = pygame.font.SysFont('Arial', SQ_SIZE // 3)  # Điều chỉnh kích thước font nếu cần

        # Tạo các dòng văn bản
        text_support1 = font_support.render("Support Keys:", True, 'white')
        text_support2 = font_support.render("•  U: Undo the last move", True, 'white')
        text_support3 = font_support.render("•  N: Toggle Negamax", True, 'white')
        text_support4 = font_support.render("•  ESC: Toggle support On/Off", True, 'white')

        # Hiển thị các dòng văn bản tại vị trí text_support
        screen.blit(text_support1, (SQ_SIZE * 3 + SQ_SIZE // 2, SQ_SIZE + SQ_SIZE // 2))
        screen.blit(text_support2, (SQ_SIZE * 3 + SQ_SIZE // 2, SQ_SIZE * 2))
        screen.blit(text_support3, (SQ_SIZE * 3 + SQ_SIZE // 2, SQ_SIZE * 2 + SQ_SIZE // 2))
        screen.blit(text_support4, (SQ_SIZE * 3 + SQ_SIZE // 2, SQ_SIZE * 3))

        resume_button = draw_button('Resume', SQ_SIZE // 3, SQ_SIZE * 9 - SQ_SIZE // 2, SQ_SIZE * 1 + SQ_SIZE // 2,
                                    SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7,0,
                                    'white', 'black', COLOR_SCREEN, 'aquamarine', COLOR_SCREEN)

        mew_game_button = draw_button('New Game', SQ_SIZE // 3,  SQ_SIZE * 9 - SQ_SIZE // 2, SQ_SIZE * 2 + SQ_SIZE // 2,
                                      SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                                  'white', 'black', COLOR_SCREEN, 'aquamarine', COLOR_SCREEN)

        main_menu_button = draw_button("Main menu", SQ_SIZE // 3,  SQ_SIZE * 9 - SQ_SIZE // 2, SQ_SIZE * 4 + SQ_SIZE // 2,
                                       SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7,0,
                                  'white', 'black', COLOR_SCREEN, 'aquamarine', COLOR_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game(SQ_SIZE)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if resume_button.collidepoint(event.pos):
                    in_support = False
                    screen.fill(COLOR_GAME)
                elif mew_game_button.collidepoint(event.pos):
                    play_sound("game-start.mp3")
                    play_game(SQ_SIZE)
                elif main_menu_button.collidepoint(event.pos):
                    main_menu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_support = False
        clock.tick(60)
        pygame.display.flip()

def setting(SQ_SIZE, size_index):
    """Hiển thị menu thiết lập"""
    # Khởi tạo kích thước ban đầu
    global WIDTH, HEIGHT, screen
    sizes = [(960, 540), (1120, 630), (1280, 720), (1440, 810), (1600, 900)]
    WIDTH, HEIGHT = sizes[size_index]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    in_settings = True
    screen.fill(COLOR_SCREEN)
    while in_settings:
        # Vẽ các nút tỉ lệ màn hình
        draw_button("", 0, SQ_SIZE * 3, SQ_SIZE * 3,
                    SQ_SIZE * 8, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                    'black', 'black', 'gray', 'gray', 'gray')

        draw_button('Resolution', SQ_SIZE // 3, SQ_SIZE * 3, SQ_SIZE * 3,
                    SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                    'black', 'black', 'gray', 'gray', 'gray')

        size_button = draw_button(f'{WIDTH}x{HEIGHT}', SQ_SIZE // 3, SQ_SIZE * 9, SQ_SIZE * 3,
                                  SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                                  'black', 'black', 'aquamarine', 'aquamarine', COLOR_SCREEN)

        back_button = draw_button('Back', SQ_SIZE // 3, SQ_SIZE * 8, SQ_SIZE * 6,
                                  SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                                  'white', 'black', COLOR_SCREEN, 'tomato', 'tomato')

        apply_button = draw_button('Apply', SQ_SIZE // 3, SQ_SIZE * 4, SQ_SIZE * 6,
                                   SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                                   'white', 'black', COLOR_SCREEN, 'light green', 'light green')

        version_button = draw_button(version, SQ_SIZE // 4, SQ_SIZE * 12, SQ_SIZE * 7,
                                     SQ_SIZE, SQ_SIZE, SQ_SIZE // 7, SQ_SIZE // 15,
                                     'white', 'white', COLOR_SCREEN, COLOR_SCREEN, COLOR_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if size_button.collidepoint(event.pos) and (event.button == 1 or
                                                            event.button == 4 or
                                                            event.button == 5):
                    if event.button == 4:
                        # Tăng đội kích thước hiện tại và vòng quay nếu cần
                        size_index = (size_index - 1) % len(sizes)
                    elif event.button == 1 or event.button == 5:
                        # Tăng chỉ số kích thước hiện tại và vòng lại nếu cần
                        size_index = (size_index + 1) % len(sizes)
                    WIDTH, HEIGHT = sizes[size_index]  # Cập nhật kích thước cửa sổ
                    apply = False
                elif apply_button.collidepoint(event.pos) and event.button == 1:
                    SQ_SIZE = HEIGHT // 8
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Thay đổi kích thước cửa sổ
                    screen.fill(COLOR_SCREEN)
                    apply = True
                elif version_button.collidepoint(event.pos) and event.button == 1:
                    code_version(SQ_SIZE)
                    screen.fill(COLOR_SCREEN)
                elif back_button.collidepoint(event.pos) and event.button == 1 and apply == True:
                    return size_index, SQ_SIZE
        clock.tick(60)
        pygame.display.flip()

def stale_check(text, SQ_SIZE):
    """Hiển thị thông báo game đã kết thúc"""
    draw_button("", 0, SQ_SIZE * 2, SQ_SIZE * 3,
                SQ_SIZE * 4, SQ_SIZE * 2, SQ_SIZE // 7, SQ_SIZE // 22,
                'white', 'black', COLOR_SCREEN, COLOR_SCREEN, 'aquamarine')

    draw_button(text, SQ_SIZE // 3, SQ_SIZE * 2, SQ_SIZE * 3 + SQ_SIZE // 2,
                SQ_SIZE * 4, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                'white', 'white', COLOR_SCREEN, COLOR_SCREEN, COLOR_SCREEN)

    new_game_button = draw_button("New game", SQ_SIZE // 3, SQ_SIZE * 2 + SQ_SIZE // 8, SQ_SIZE * 4 + SQ_SIZE // 4,
                                  SQ_SIZE * 2 - SQ_SIZE // 4, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                                  'white', 'black', COLOR_SCREEN, 'light green', 'light green')

    quit_button = draw_button("Quit", SQ_SIZE // 3, SQ_SIZE * 4 + SQ_SIZE // 8, SQ_SIZE * 4 + SQ_SIZE // 4,
                              SQ_SIZE * 2 - SQ_SIZE // 4, SQ_SIZE // 2, SQ_SIZE // 7, SQ_SIZE // 22,
                              'white', 'black', COLOR_SCREEN, 'tomato', 'tomato')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if new_game_button.collidepoint(event.pos):
                play_sound("game-start.mp3")
                play_game(SQ_SIZE)
            elif quit_button.collidepoint(event.pos):
                main_menu()

def play_game(SQ_SIZE):
    """Phần giao diện chơi cờ"""
    global text

    screen.fill(COLOR_GAME)
    game_state = GameState()
    valid_moves = game_state.get_valid_moves()
    move_made = False
    animate = False
    load_images(SQ_SIZE)
    load_captured_images(SQ_SIZE)
    load_promote_images(SQ_SIZE)

    in_game = True
    square_selected = ()
    player_clicks = []
    game_over = False
    sound_played = False
    not_negamax = True

    while in_game:
        human_turn = (game_state.white_to_move and True) or (not game_state.white_to_move and not_negamax)
        # Tạo văn bản "Negamax" với màu trắng
        font = pygame.font.SysFont('Arial', SQ_SIZE // 3, True)
        negamax_text = font.render("Negamax:", True, 'white')

        # Tạo văn bản "on" hoặc "off" với màu tương ứng
        if not_negamax:
            status_text = font.render("Off", True, 'tomato')
        else:
            status_text = font.render("On", True, 'chartreuse')

        # Vẽ nút Negamax (nền)
        negamax_button = draw_button('', SQ_SIZE // 3, SQ_SIZE * 8 + SQ_SIZE // 2, SQ_SIZE // 4,
                                     SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                                     'white', 'black', COLOR_SCREEN, COLOR_SCREEN, 'black')

        # Hiển thị văn bản "Negamax" và "on/off" trên nút
        screen.blit(negamax_text, (SQ_SIZE * 9 - SQ_SIZE // 2 + SQ_SIZE // 8, SQ_SIZE // 2 - SQ_SIZE // 5))
        screen.blit(status_text, (SQ_SIZE * 10 - SQ_SIZE // 15, SQ_SIZE // 2 - SQ_SIZE // 5))

        undo_button = draw_button('Undo', SQ_SIZE // 3, SQ_SIZE * 11, SQ_SIZE // 4,
                                  SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                                  'gold', 'black', COLOR_SCREEN, 'gold', 'black')

        support_button = draw_button('≡', SQ_SIZE // 3, SQ_SIZE * 13 + SQ_SIZE // 4, SQ_SIZE // 4,
                                     SQ_SIZE / 2, SQ_SIZE // 2, SQ_SIZE // 5, 0,
                                     'grey', 'black', COLOR_SCREEN, 'grey', 'black')

        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game(SQ_SIZE)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if support_button.collidepoint(event.pos):
                        support(SQ_SIZE)
                        screen.fill(COLOR_GAME)
                    elif undo_button.collidepoint(event.pos):
                        if len(game_state.move_log) > 0:
                            game_state.undo_move()
                            valid_moves = game_state.get_valid_moves()
                            square_selected = ()
                            player_clicks = []
                            move_made = False
                            animate = False
                            play_sound("move-self.mp3")
                    elif negamax_button.collidepoint(event.pos):
                        not_negamax = not not_negamax
                        if not_negamax:
                            for _ in range(2):
                                play_sound("negamax-off.mp3")
                                pygame.time.delay(100)
                        else:
                            play_sound("negamax-on.mp3")


                    if not game_over:
                        location = pygame.mouse.get_pos()
                        column = location[0] // SQ_SIZE
                        row = location[1] // SQ_SIZE
                        if square_selected == (row, column) or column >= 8:
                            square_selected = ()
                            player_clicks = []
                        else:
                            square_selected = (row, column)
                            player_clicks.append(square_selected)
                        if len(player_clicks) == 2:
                            move = Move(player_clicks[0], player_clicks[1], game_state.board)
                            for i in range(len(valid_moves)):
                                if move == valid_moves[i]:
                                    game_state.make_move(valid_moves[i], SQ_SIZE)
                                    move_made = True
                                    animate = True
                                    square_selected = ()
                                    player_clicks = []

                            if not move_made:
                                player_clicks = [square_selected]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        support(SQ_SIZE)
                        screen.fill(COLOR_GAME)
                    elif event.key == pygame.K_n:
                        not_negamax = not not_negamax
                        if not_negamax:
                            for _ in range(2):
                                play_sound("negamax-off.mp3")
                                pygame.time.delay(100)
                        else:
                            play_sound("negamax-on.mp3")
                    elif event.key == pygame.K_u:
                        if len(game_state.move_log) > 0:
                            game_state.undo_move()
                            valid_moves = game_state.get_valid_moves()
                            square_selected = ()
                            player_clicks = []
                            move_made = False
                            animate = False
                            play_sound("move-self.mp3")

        # Tìm nước đi của AI
        if not game_over and not human_turn:
            game_state.negamax_turn = True
            AI_move = find_best_move(game_state, valid_moves, SQ_SIZE)
            if AI_move is None:
                AI_move = find_random_move(valid_moves)
            game_state.make_move(AI_move, SQ_SIZE)
            move_made = True
            animate = True
            game_state.negamax_turn = False

        if move_made:
            if animate:
                animate_move(game_state.move_log[-1], screen, game_state.board, clock, game_state, SQ_SIZE)
                animate = False
                play_sound("move-self.mp3")
            valid_moves = game_state.get_valid_moves()
            move_made = False

        draw_game_state(screen, game_state, square_selected, SQ_SIZE)

        if (game_state.checkmate or
                game_state.stalemate or
                game_state.insufficient_material()):
            game_over = True

            # Phát âm thanh kết thúc game chỉ một lần
            if not sound_played:
                play_sound("game-end.mp3")
                sound_played = True

            # Hiển thị kết quả trò chơi
            if game_state.stalemate:
                text = 'Stalemate'
            elif game_state.checkmate:
                if game_state.white_to_move:
                    text = 'Black wins by checkmate'
                else:
                    text = 'White wins by checkmate'
            stale_check(text, SQ_SIZE)

        clock.tick(60)
        pygame.display.flip()

def main_menu():
    """Hiển thị menu chính"""
    running = True
    global WIDTH, HEIGHT, SQ_SIZE, screen
    size_index = 3  # Chỉ số kích thước hiện tại
    SQ_SIZE = HEIGHT // 8
    screen.fill(COLOR_SCREEN)
    while running:
        draw_button('', SQ_SIZE // 3, SQ_SIZE * 6 - SQ_SIZE // 4, SQ_SIZE * 3  + SQ_SIZE // 4,
                    SQ_SIZE * 3 - SQ_SIZE // 2, SQ_SIZE * 3, SQ_SIZE // 7, SQ_SIZE // 22,
                    'white', 'white', COLOR_SCREEN, COLOR_SCREEN, 'grey')

        play_button = draw_button('New Game', SQ_SIZE // 3, SQ_SIZE * 6, SQ_SIZE * 3 + SQ_SIZE // 2,
                                  SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                                  'white', 'black', COLOR_SCREEN, 'aquamarine', COLOR_SCREEN)

        setting_button = draw_button('Setting', SQ_SIZE // 3, SQ_SIZE * 6, SQ_SIZE * 4 + SQ_SIZE // 2,
                                     SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                                     'white', 'black', COLOR_SCREEN, 'aquamarine', COLOR_SCREEN)

        quit_button = draw_button('Quit', SQ_SIZE // 3, SQ_SIZE * 6, SQ_SIZE * 5 + SQ_SIZE // 2,
                                  SQ_SIZE * 2, SQ_SIZE // 2, SQ_SIZE // 7, 0,
                                  'white', 'black', COLOR_SCREEN, 'tomato', COLOR_SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.collidepoint(event.pos):
                    play_sound("game-start.mp3")
                    play_game(SQ_SIZE)
                elif setting_button.collidepoint(event.pos):
                    size_index, SQ_SIZE = setting(SQ_SIZE, size_index)  # Cập nhật size_index và SQ_SIZE từ setting()
                    WIDTH, HEIGHT = [(960, 540), (1120, 630), (1280, 720), (1440, 810), (1600, 900)][size_index]
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Áp dụng tỉ lệ mới
                    screen.fill(COLOR_SCREEN)  # Xóa màn hình trước khi tiếp tục vẽ lại
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
