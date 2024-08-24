from vsAI import *
from Game import *
from Engine import *
from Constants import *
from ChessAI import *
import pygame
import os

pygame.init()
AI = False

# Tải hình ảnh icon (đảm bảo rằng đường dẫn tới file .ico đúng)
icon_path = os.path.join('images', 'logo.png')
icon = pygame.image.load(icon_path)

# Thiết lập icon cho cửa sổ
pygame.display.set_icon(icon)

# Thiết lập tiêu đề cửa sổ
pygame.display.set_caption('Chess_Python by Nguyen Le Van Dung')

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def play_game(AI):
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

def settings_menu():
    """Hiển thị menu thiết lập"""
    global WIDTH, HEIGHT, SQ_SIZE, screen
    running = True
    selected_aspect_ratio = '1280x720'  # Mặc định là 1280x720

    while running:
        a_button = draw_button('960x540', SQ_SIZE * 4, SQ_SIZE * 2 + 3 * BUTTON_HEIGHT,
                               'grey', 'light green', 'green')
        b_button = draw_button('1120x630', SQ_SIZE * 8, SQ_SIZE * 2 + 3 * BUTTON_HEIGHT,
                               'grey', 'light green', 'green')
        c_button = draw_button('1280x720', SQ_SIZE * 4, SQ_SIZE * 2 + 5 * BUTTON_HEIGHT,
                               'grey', 'light green', 'green')
        d_button = draw_button('1440x810', SQ_SIZE * 8, SQ_SIZE * 2 + 5 * BUTTON_HEIGHT,
                               'grey', 'light green', 'green')
        back_button = draw_button('Back', SQ_SIZE * 6, SQ_SIZE * 2 + 7 * BUTTON_HEIGHT,
                                  'grey', 'red', 'dark red')

        # Vẽ viền xanh quanh tùy chọn được chọn
        if selected_aspect_ratio == '960x540':
            pygame.draw.rect(screen, 'yellow', pygame.Rect(SQ_SIZE * 4, SQ_SIZE * 2 + 3 * BUTTON_HEIGHT, SQ_SIZE * 2, SQ_SIZE // 2), 4)
        elif selected_aspect_ratio == '1120x630':
            pygame.draw.rect(screen, 'yellow', pygame.Rect(SQ_SIZE * 8, SQ_SIZE * 2 + 3 * BUTTON_HEIGHT, SQ_SIZE * 2, SQ_SIZE // 2), 4)
        elif selected_aspect_ratio == '1280x720':
            pygame.draw.rect(screen, 'yellow', pygame.Rect(SQ_SIZE * 4, SQ_SIZE * 2 + 5 * BUTTON_HEIGHT, SQ_SIZE * 2, SQ_SIZE // 2), 4)
        elif selected_aspect_ratio == '1440x810':
            pygame.draw.rect(screen, 'yellow', pygame.Rect(SQ_SIZE * 8, SQ_SIZE * 2 + 5 * BUTTON_HEIGHT, SQ_SIZE * 2, SQ_SIZE // 2), 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if a_button.collidepoint(event.pos):
                    selected_aspect_ratio = '960x540'
                elif b_button.collidepoint(event.pos):
                    selected_aspect_ratio = '1120x630'
                elif c_button.collidepoint(event.pos):
                    selected_aspect_ratio = '1280x720'
                elif d_button.collidepoint(event.pos):
                    selected_aspect_ratio = '1440x810'
                elif back_button.collidepoint(event.pos):
                    return

                # Cập nhật SQ_SIZE và làm mới cửa sổ
                SQ_SIZE = HEIGHT // 8
                screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

def main_menu():
    """Hiển thị menu chính"""
    running = True
    while running:
        if not pygame.display.get_surface():
            return
        screen.fill('grey22')

        pvp_button = draw_button('vs Friend', SQ_SIZE * 6, SQ_SIZE * 2 + BUTTON_HEIGHT,
                                 'grey', 'light green', 'dark green')
        negamax_button = draw_button('vs Negamax', SQ_SIZE * 6, SQ_SIZE * 2 + 3 * BUTTON_HEIGHT, 'grey', 'light green', 'green')
        exit_button = draw_button('Exit', SQ_SIZE * 6, SQ_SIZE * 2 + 7 * BUTTON_HEIGHT,
                                  'grey', 'tomato', 'dark red')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # True: Player vs. Player
                # False: Player vs. Negamax
                if pvp_button.collidepoint(event.pos):
                    AI = True
                    play_game(AI)
                elif negamax_button.collidepoint(event.pos):
                    AI = False
                    play_game_AI(AI)
                elif exit_button.collidepoint(event.pos):
                    running = False

        try:
            pygame.display.flip()
        except pygame.error:
            pass
        clock.tick(FPS)

if __name__ == '__main__':
    main_menu()
    if pygame.error:
        pass
