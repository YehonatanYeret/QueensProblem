import pygame

# Colors and GUI parameters
N = 8
FPS_SOLUTION = 590
FPS = 5
WHITE = (255, 255, 255)
LIGHT_BROWN = (181, 101, 29)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)
BRIGHT_RED = (255, 102, 102)
LIGHT_BEIGE = (245, 245, 220)
SOFT_BROWN = (210, 180, 140)

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
MARGIN = 20
table_width = WINDOW_WIDTH - 2 * MARGIN
table_height = WINDOW_HEIGHT - 2 * MARGIN

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Queens Problem")
clock = pygame.time.Clock()


# GUI function to initialize the board
def init(n):
    global WINDOW_WIDTH, WINDOW_HEIGHT, MARGIN, table_width, table_height, N
    # Colors and GUI parameters
    N = n
    MARGIN = N
    table_width = WINDOW_WIDTH - 2 * MARGIN
    table_height = WINDOW_HEIGHT - 2 * MARGIN


# GUI function to print the board
def GUI_print_board(board):
    screen.fill(DARK_GRAY)  # Fill the background with the dark gray color

    # Draw the grid with alternating colors for the chessboard pattern
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                color = LIGHT_BEIGE
            else:
                color = SOFT_BROWN
            pygame.draw.rect(screen, color, (MARGIN + j * table_width / N, MARGIN + i * table_height / N,
                                             table_width / N, table_height / N))

    # Draw the queens
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                pygame.draw.circle(screen, BRIGHT_RED, (MARGIN + j * table_width // N + table_width // (2 * N),
                                                        MARGIN + i * table_height // N + table_height // (2 * N)),
                                   table_width // (N * 4))

    pygame.display.flip()
    clock.tick(FPS)
