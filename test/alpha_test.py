import pygame

pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 820
IMAGE_SIZE = (100, 100)
IMAGE_SIZE_SMALL = (50, 50)
FPS = 60

# Initialize Pygame screen and font
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Chess by Nguyen Le Van Dung')
font = pygame.font.SysFont('roboto', 20)
medium_font = pygame.font.SysFont('roboto', 25)
big_font = pygame.font.SysFont('roboto', 40)
timer = pygame.time.Clock()

# Game variables
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

# Game state
turn_step = 0
selection = None
valid_moves = []
counter = 0
winner = ''
game_over = False

# Load and scale images
def load_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)

black_images = {
    'queen': load_image('../assets/images/black_queen.png', IMAGE_SIZE),
    'king': load_image('../assets/images/black_king.png', IMAGE_SIZE),
    'rook': load_image('../assets/images/black_rook.png', IMAGE_SIZE),
    'bishop': load_image('../assets/images/black_bishop.png', IMAGE_SIZE),
    'knight': load_image('../assets/images/black_knight.png', IMAGE_SIZE),
    'pawn': load_image('../assets/images/black_pawn.png', IMAGE_SIZE),
}
white_images = {
    'queen': load_image('../assets/images/white_queen.png', IMAGE_SIZE),
    'king': load_image('../assets/images/white_king.png', IMAGE_SIZE),
    'rook': load_image('../assets/images/white_rook.png', IMAGE_SIZE),
    'bishop': load_image('../assets/images/white_bishop.png', IMAGE_SIZE),
    'knight': load_image('../assets/images/white_knight.png', IMAGE_SIZE),
    'pawn': load_image('../assets/images/white_pawn.png', IMAGE_SIZE),
}

# Draw board
def draw_board():
    for i in range(8):
        for j in range(8):
            color = '#ebecd0' if (i + j) % 2 == 0 else '#739552'
            pygame.draw.rect(screen, color, [i * 100, j * 100, 100, 100])
    pygame.draw.line(screen, 'grey', [910, 740], [910, 0], 3)
    pygame.draw.line(screen, 'grey', [800, 810], [0, 810], 20)
    pygame.draw.line(screen, 'grey', [810, 840], [810, 0], 20)
    status_text = ['White turn', 'White turn', 'Black turn', 'Black turn']
    rect_color = 'black' if turn_step < 2 else 'white'
    text_color = '#e9e9e9' if turn_step < 2 else '#545454'
    pygame.draw.rect(screen, rect_color, [820, 740, 820, 740])
    screen.blit(big_font.render(status_text[turn_step], True, text_color), (840, 770))
    # Draw row labels
    for i in range(8):
        text = medium_font.render(chr(ord('A') + i), True, 'black')
        screen.blit(text, (15 + i * 100 + 100 // 3, 803))
    # Draw column labels
    for i in range(8):
        text = medium_font.render(str(8 - i), True, 'black')
        screen.blit(text, (807, 10 + i * 100 + 100 // 3))

# Draw pieces
def draw_pieces():
    def draw_piece_list(pieces, locations, images, selection_check):
        for i, piece in enumerate(pieces):
            image = images[piece]
            screen.blit(image, (locations[i][0] * 100, locations[i][1] * 100))
            if selection_check(i):
                pygame.draw.rect(screen, 'blue', [locations[i][0] * 100 + 1, locations[i][1] * 100 + 1, 100, 100], 5)

    draw_piece_list(white_pieces, white_locations, white_images, lambda i: turn_step < 2 and selection == i)
    draw_piece_list(black_pieces, black_locations, black_images, lambda i: turn_step >= 2 and selection == i)

# Draw move indication
def draw_move_indicator(old_pos, new_pos):
    if old_pos:
        pygame.draw.rect(screen, 'yellow', [old_pos[0] * 100, old_pos[1] * 100, 100, 100], 5)
    if new_pos:
        pygame.draw.rect(screen, 'yellow', [new_pos[0] * 100, new_pos[1] * 100, 100, 100], 5)

# Check if a position is valid
def is_valid_position(pos):
    x, y = pos
    return 0 <= x < 8 and 0 <= y < 8

# Main loop
def main():
    global turn_step, selection, valid_moves, counter, winner, game_over
    old_pos = None
    new_pos = None
    selected_piece = None
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos[0] // 100, pos[1] // 100

                if is_valid_position((x, y)):
                    if selection is not None:
                        new_pos = (x, y)
                        if selected_piece and (new_pos != old_pos):
                            # Update position of the selected piece
                            if turn_step < 2:
                                index = selection
                                white_locations[index] = new_pos
                            else:
                                index = selection
                                black_locations[index] = new_pos
                            old_pos = selected_piece
                            selection = None
                            selected_piece = None
                            turn_step = (turn_step + 1) % 4
                    else:
                        # Select a piece
                        if turn_step < 2 and (x, y) in white_locations:
                            selection = white_locations.index((x, y))
                            selected_piece = (x, y)
                        elif turn_step >= 2 and (x, y) in black_locations:
                            selection = black_locations.index((x, y))
                            selected_piece = (x, y)
                        old_pos = None

        screen.fill('white')
        draw_board()
        draw_pieces()
        draw_move_indicator(old_pos, new_pos)
        pygame.display.flip()
        timer.tick(FPS)

if __name__ == "__main__":
    main()
