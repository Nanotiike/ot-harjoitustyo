from random import randint

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.player_board = self.create_player_board()
        self.mistakes = 0

    def print_board(self, board):
        # Leftover from earlier version. Prints the board to the console
        c = 0
        for i in range(len(board)):
            r = 0
            for j in range(len(board[i])):
                print(board[i][j], end=" ")
                r += 1
                if r == 3:
                    print("|", end=" ")
                    r = 0
            print()
            c += 1
            if c == 3:
                print("---------------------")
                c = 0

    def check_number(self, y, x, number):
        for i in range(len(self.board)):
            if self.board[y][i] == number:
                return True

        for i in range(len(self.board)):
            if self.board[i][x] == number:
                return True

        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.board[y0+i][x0+j] == number:
                    return True

        return False

    def create_player_board(self):
        # Creates a player board with 17 clues
        temp_board =[[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # Minimum number of clues that result in a unique solution is 17. Number could be changed later
        clues = 17
        while clues > 0:
            x = randint(0, 8)
            y = randint(0, 8)
            if temp_board[y][x] == 0:
                temp_board[y][x] = self.board[y][x]
                clues -= 1

        return temp_board

    def make_move(self, y, x, number):
        # Checks if the move is valid and makes the move
        if self.player_board[y][x] == 0:
            if self.board[y][x] == number:
                self.player_board[y][x] = number
                return 0
            else:
                self.mistakes += 1
                return 1
        else:
            return 2