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
    screen_size = (544, 610)
    screen = pygame.display.set_mode((screen_size))
    pygame.display.set_caption("Sudoku")
    font = pygame.font.SysFont("Arial", 30)
    font2 = pygame.font.SysFont("Arial", 20)
    x = -1
    y = -1

    running = True

    while running:
        for event in pygame.event.get():
            draw_backround(screen, x, y)
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
                if 0 < event.key-48 < 10 and -1<x<9 and -1<y<9:
                    result = game_board.make_move(y, x, event.key-48)
                    if result != 0:
                        if result == 1:
                            pygame.draw.rect(screen, (255, 255, 255), (172, 247, 200, 50))
                            pygame.draw.rect(screen, (0, 0, 0), (172, 247, 200, 50), 3)
                            text = font2.render("Wrong number!", True, (0, 0, 0))
                            screen.blit(text, (202, 259))
                        elif result == 2:
                            pygame.draw.rect(screen, (255, 255, 255), (97, 247, 350, 50))
                            pygame.draw.rect(screen, (0, 0, 0), (97, 247, 350, 50), 3)
                            text = font2.render("That square already has a number!", True, (0, 0, 0))
                            screen.blit(text, (117, 259))
                        pygame.display.update()
                        pygame.time.delay(2000)

def draw_backround(screen, x, y):
    # Draw the backround blue and draw a white board with a grid of black lines
    screen.fill((212, 235, 242))
    pygame.draw.rect(screen, (255, 255, 255), (20, 20, 504, 504))
    if -1<x<9 and -1<y<9:
        pygame.draw.rect(screen, (190, 190, 190), (20+x*56, 20+y*56, 56, 56))
    pygame.draw.rect(screen, (0, 0, 0), (20, 20, 504, 504), 3)
    i = 1
    while (i*56)<504:
        line_width = 3 if i%3 > 0 else 7
        pygame.draw.line(screen, (0, 0, 0), (20+i*56, 20), (20+i*56, 524), line_width)
        pygame.draw.line(screen, (0, 0, 0), (20, 20+i*56), (524, 20+i*56), line_width)
        i+=1
    pygame.draw.rect(screen, (255, 255, 255), (20, 534, 504, 70))
    pygame.draw.rect(screen, (0, 0, 0), (20, 534, 504, 70), 3)
    font2 = pygame.font.SysFont("Arial", 20)
    text = font2.render("Press your mouse key on a square to select it and then", True, (0, 0, 0))
    text2 = font2.render("press a number from 1 to 9 to enter a number.", True, (0, 0, 0))
    screen.blit(text, (25, 539))
    screen.blit(text2, (25, 564))

def draw_numbers(screen, font, game_board):
    # Draw the numbers from the board
    for i in range(9):
        for j in range(9):
            if game_board.player_board[i][j] != 0:
                text = font.render(str(game_board.player_board[i][j]), True, (0, 0, 0))
                screen.blit(text, (20+j*56+20, 20+i*56+12))

if __name__ == '__main__':
    main()
