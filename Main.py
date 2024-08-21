from Game import *
from Constants import *
import pygame as p

p.init()

# Khởi tạo màn hình
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Chess Main Menu')
clock = p.time.Clock()


def draw_button(text, x, y, color, hover_color):
    """Vẽ nút với màu sắc và vị trí đã chỉ định"""
    mouse_pos = p.mouse.get_pos()
    button_rect = p.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    if button_rect.collidepoint(mouse_pos):
        p.draw.rect(screen, hover_color, button_rect)
    else:
        p.draw.rect(screen, color, button_rect)

    text_surface = large_font.render(text, True, 'black')
    screen.blit(text_surface, text_surface.get_rect(center=button_rect.center))
    return button_rect


def pve_menu():
    """Hiển thị menu PvE"""
    running = True
    while running:
        screen.fill('grey22')

        p.draw.rect(screen, 'grey22', p.Rect(SQ_SIZE * 10, SQ_SIZE * 9, SQ_SIZE * 3, SQ_SIZE))
        text_version = version_font.render(version, True, p.Color('white'))
        screen.blit(text_version, (SQ_SIZE * 11, SQ_SIZE * 9))

        '''easy_button = draw_button('Easy', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 2 * BUTTON_HEIGHT,
                                  'grey', 'green')
        medium_button = draw_button('Medium', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 4 * BUTTON_HEIGHT,
                                    'grey', 'green')
        hard_button = draw_button('Hard', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 6 * BUTTON_HEIGHT,
                                  'grey', 'green')'''
        back_button = draw_button('Back', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 8 * BUTTON_HEIGHT,
                                  'grey', 'red')
        update_button = draw_button('Update soon!', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 4 * BUTTON_HEIGHT,
                                    'grey', 'green')

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                '''if easy_button.collidepoint(event.pos):
                    print('Update soon!')
                elif medium_button.collidepoint(event.pos):
                    print('Update soon!')
                elif hard_button.collidepoint(event.pos):
                    print('Update soon!')'''
                if update_button.collidepoint(event.pos):
                    pass
                elif back_button.collidepoint(event.pos):
                    return

        p.display.flip()
        clock.tick(FPS)

def play_game():
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
        replay_button = draw_button('Replay', SQ_SIZE * 8.2, SQ_SIZE + BUTTON_HEIGHT / 2,
                                    'light grey', 'green')

        exit_button = draw_button('Exit', SQ_SIZE * 10.35, SQ_SIZE + BUTTON_HEIGHT / 2,
                                  'light grey', 'red')
        # Menu buttons
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

            # Mouse handler
            elif event.type == p.MOUSEBUTTONDOWN:
                if replay_button.collidepoint(event.pos):
                    game_state = GameState()
                    valid_moves = game_state.get_valid_moves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    game_over = False

                    screen.fill(p.Color('dark grey'))
                elif exit_button.collidepoint(event.pos):
                    return
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

    p.quit()


def main_menu():
    """Hiển thị menu chính"""
    running = True
    while running:
        if not p.display.get_surface():
            return
        screen.fill('grey22')

        p.draw.rect(screen, 'grey22', p.Rect(SQ_SIZE * 10, SQ_SIZE * 9, SQ_SIZE * 3, SQ_SIZE))
        text_version = version_font.render(version, True, p.Color('white'))
        screen.blit(text_version, (SQ_SIZE * 11, SQ_SIZE * 9))

        pvp_button = draw_button('PvP', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 2 * BUTTON_HEIGHT,
                                 'grey', 'green')
        pve_button = draw_button('PvE', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 4 * BUTTON_HEIGHT,
                                 'grey', 'green')
        exit_button = draw_button('Exit', SQ_SIZE * 7 - SQ_SIZE * 2, SQ_SIZE * 2 + 6 * BUTTON_HEIGHT,
                                  'grey', 'red')

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                if pvp_button.collidepoint(event.pos):
                    play_game()
                elif pve_button.collidepoint(event.pos):
                    pve_menu()
                elif exit_button.collidepoint(event.pos):
                    running = False

        try:
            p.display.flip()
        except p.error:
            pass
        clock.tick(FPS)


if __name__ == '__main__':
    main_menu()
    if p.error:
        pass
