import random
import math
import pygame
import GUI_queens as GUI

# Parameters for the Simulated Annealing
initial_temp = 1000
max_iterations = 15000


# Create random board with x queens
def rnd_board(x):
    # returns a board x*x with queens in random cols
    board = []
    for i in range(x):
        board.append(random.randrange(x))
    return board


# Print the board to the console
def print_board(board):
    # prints the board: #= empty cell Q=a queen
    print()
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r] == c:
                print('Q', end='')
            else:
                print('#', end='')
        print()
    return


# Returns the number of threats in the board
def threats(board):
    # returns number of threats in board
    count = 0
    for i in range(0, len(board) - 1):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                count = count + 1
    return count


# Swap two random queens
def swap_two_queens(board):
    new_board = board[:]
    i, j = random.sample(range(len(board)), 2)
    new_board[i], new_board[j] = new_board[j], new_board[i]
    return new_board


# Cooling schedule: function to reduce temperature
def schedule(t):
    return 1000 * (0.995 ** t)


# Simulated Annealing algorithm
def simulated_annealing(queens_matrix):
    GUI.GUI_print_board(queens_matrix)
    num_queens = len(queens_matrix)

    # Initial random board
    current_board = list(range(num_queens))
    random.shuffle(current_board)
    current_threats = threats(current_board)

    best_board = current_board
    best_threats = current_threats

    current = current_board
    best_distances = []

    for t in range(max_iterations):
        T = schedule(t)
        if T == 0:
            break

        next_board = swap_two_queens(current)
        next_threats = threats(next_board)

        delta_E = next_threats - threats(current)

        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            current = next_board
            current_threats = next_threats

        if current_threats < best_threats:
            best_board = current
            best_threats = current_threats
            GUI.GUI_print_board(best_board)

        best_distances.append(best_threats)

        # Print the current best threats at each iteration
        print(f"Iteration {t + 1}: Best Threats = {best_threats}")

        if best_threats == 0:
            break

    return best_board, best_threats


# Run the Simulated Annealing algorithm
def main():
    N = 20
    GUI.init(N)
    best_board, best_threats = simulated_annealing(rnd_board(N))

    if best_threats == 0:
        print("\nSolution found:")
    else:
        print("\nNo solution found.")
        pygame.quit()
        quit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()
