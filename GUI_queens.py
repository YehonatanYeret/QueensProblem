import pygame

# Colors and GUI parameters
N = 8
FPS_SOLUTION = 590
FPS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLACK = (121, 119, 125)
BLUE = (104, 185, 222)
LIGHT_RED = (171, 47, 31)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)
BRIGHT_RED = (255, 0, 0)
# Colors and GUI parameters
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
MARGIN = 500 // N
table_width = WINDOW_WIDTH - 2 * MARGIN
table_height = WINDOW_HEIGHT - 2 * MARGIN

# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Queens Problem")
clock = pygame.time.Clock()


# GUI function to initialize the board
def init(n):
    global WINDOW_WIDTH, WINDOW_HEIGHT, MARGIN, table_width, table_height, N
    # Colors and GUI parameters
    N = n
    WINDOW_WIDTH = 720
    WINDOW_HEIGHT = 720
    MARGIN = 500 // N
    table_width = WINDOW_WIDTH - 2 * MARGIN
    table_height = WINDOW_HEIGHT - 2 * MARGIN


# GUI function to print the board
def GUI_print_board(board):
    pygame.draw.rect(screen, DARK_GRAY, (MARGIN, MARGIN, table_width, table_height))

    # Draw the grid
    for i in range(N + 1):
        pygame.draw.line(screen, LIGHT_GRAY, (i * table_width // N + MARGIN, MARGIN),
                         (i * table_width // N + MARGIN, WINDOW_HEIGHT - MARGIN), 1)
        pygame.draw.line(screen, LIGHT_GRAY, (MARGIN, i * table_height // N + MARGIN),
                         (WINDOW_WIDTH - MARGIN, i * table_height // N + MARGIN), 1)

    # Draw the queens
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                pygame.draw.circle(screen, BRIGHT_RED, (MARGIN + j * table_width // N + table_width // (2 * N),
                                                        MARGIN + i * table_height // N + table_height // (2 * N)),
                                   table_width // (N * 4))

    pygame.display.flip()
    clock.tick(FPS)
