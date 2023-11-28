from sudoku import Sudoku
from sudoku_generator import generate_sudoku
import re

def main():
    game_board = Sudoku(generate_sudoku())
    # game_board.print_board(game_board.board)
    # game_board.print_board(game_board.player_board)

    running = True

    while running:
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
            print("Invalid input")

if __name__ == '__main__':
    main()
