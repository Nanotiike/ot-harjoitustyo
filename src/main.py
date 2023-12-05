from sudoku import Sudoku
from sudoku_generator import generate_sudoku
import pygame
import re

def main():
    # Generate sudoku board and initialize the game
    random_board = generate_sudoku()
    game_board = Sudoku(random_board.board)

    # Initialize pygame
    pygame.init()
    screen_size = (544, 600)
    screen = pygame.display.set_mode((screen_size))
    pygame.display.set_caption("Sudoku")
    font = pygame.font.SysFont("Arial", 30)
    x = 0
    y = 0

    running = True

    while running:
        for event in pygame.event.get():
            draw_backround(screen)
            draw_numbers(screen, font, game_board)
            pygame.display.update()
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                x = (position[0]-20)//56
                y = (position[1]-20)//56
                print(x, y, position)
            if event.type == pygame.KEYDOWN:
                print(event.key, x, y)
                if 0 < event.key-48 < 10:
                    print(game_board.make_move(y, x, event.key-48))

    """while running:
        if game_board.player_board == game_board.board:
            print("You won!")
            running = False
            break
        game_board.print_board(game_board.player_board)
        player_move = input("Enter the coordinates (1-9) and the number you want to input (1-9), in the form 'x y number', or exit if you want to quit: ")
        if player_move == "exit":
            running = False
            break
        elif bool(re.match("[1-9] [1-9] [1-9]", player_move)) == True:
            x, y, number = player_move.split()
            print(game_board.make_move(int(y)-1, int(x)-1, int(number)))
        else:
            print("Invalid input")"""

def draw_backround(screen):
    # Draw the backround blue and draw a white board with a grid of black lines
    screen.fill((212, 235, 242))
    pygame.draw.rect(screen, (255, 255, 255), (20, 20, 504, 504))
    pygame.draw.rect(screen, (0, 0, 0), (20, 20, 504, 504), 3)
    i = 1
    while (i*56)<504:
        line_width = 3 if i%3 > 0 else 7
        pygame.draw.line(screen, (0, 0, 0), (20+i*56, 20), (20+i*56, 524), line_width)
        pygame.draw.line(screen, (0, 0, 0), (20, 20+i*56), (524, 20+i*56), line_width)
        i+=1

def draw_numbers(screen, font, game_board):
    # Draw the numbers from the board
    for i in range(9):
        for j in range(9):
            if game_board.player_board[i][j] != 0:
                text = font.render(str(game_board.player_board[i][j]), True, (0, 0, 0))
                screen.blit(text, (20+j*56+20, 20+i*56+12))

if __name__ == '__main__':
    main()
