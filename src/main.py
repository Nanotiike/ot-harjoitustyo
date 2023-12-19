from sudoku import Sudoku
from sudoku_generator import Generate_sudoku
from game_loop import Game_loop
from clock import Clock
from renderer import Renderer
import pygame

def main():
    # Generate sudoku board
    random_board = Generate_sudoku()
    random_board.randomize_sudoku()
    game_board = Sudoku(random_board.board)

    # Initialize pygame
    pygame.init()
    screen_size = (544, 650)
    screen = pygame.display.set_mode((screen_size))
    pygame.display.set_caption("Sudoku")
    font = "Arial"
    clock = Clock()
    renderer = Renderer(screen, font, game_board)

    game_loop = Game_loop(game_board, renderer, clock)
    game_loop.start()


if __name__ == '__main__':
    main()
