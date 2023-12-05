from random import shuffle, sample

class Generate_sudoku:
    def __init__(self):
        # Generate a random sudoku board
        # Return a 9x9 list
        # start with a fully made sudoku board
        self.board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [4, 5, 6, 7, 8, 9, 1, 2, 3],
                     [7, 8, 9, 1, 2, 3, 4, 5, 6],
                     [2, 3, 1, 5, 6, 4, 8, 9, 7],
                     [5, 6, 4, 8, 9, 7, 2, 3, 1],
                     [8, 9, 7, 2, 3, 1, 5, 6, 4],
                     [3, 1, 2, 6, 4, 5, 9, 7, 8],
                     [6, 4, 5, 9, 7, 8, 3, 1, 2],
                     [9, 7, 8, 3, 1, 2, 6, 4, 5]]
    
    def shuffle_numbers(self):
        # shuffle the numbers. So for example 1 becomes 5, 2 becomes 9, etc.
        temp_board = []
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffled_numbers = sample(numbers, len(numbers))
        for i in range(9):
            temp_board.append([])
            for j in range(9):
                for k in numbers:
                    if self.board[i][j] == k:
                        position_number = numbers.index(k)
                        temp_board[i].append(shuffled_numbers[position_number])

        self.board = temp_board

    def shuffle_rows(self):
        # shuffle the rows
        temp_board = []
        rows1 = sample([0, 1, 2], 3)
        rows2 = sample([3, 4, 5], 3)
        rows3 = sample([6, 7, 8], 3)
        rows = rows1+rows2+rows3
        for i in rows:
            temp_board.append(self.board[i])

        self.board = temp_board

    def shuffle_columns(self):
        # shuffle the columns
        temp_board = [[], [], [], [], [], [], [], [], []]
        columns1 = sample([0, 1, 2], 3)
        columns2 = sample([3, 4, 5], 3)
        columns3 = sample([6, 7, 8], 3)
        columns = columns1+columns2+columns3
        for i in columns:
            for j in range(9):
                temp_board[j].append(self.board[j][i])

        self.board = temp_board

    def shuffle_3x_rows(self):
        # shuffle the 3x rows
        temp_board = []
        rows = sample([0, 3, 6], 3)
        for i in rows:
            for j in range(3):
                temp_board.append(self.board[i+j])

        self.board = temp_board

    def shuffle_3x_columns(self):
        # shuffle the 3x columns
        temp_board = [[], [], [], [], [], [], [], [], []]
        columns = sample([0, 3, 6], 3)
        for i in columns:
            for j in range(3):
                for k in range(9):
                    temp_board[k].append(self.board[k][i+j])

        self.board = temp_board
    
    def randomize_sudoku(self):
        # shuffle the numbers, rows, columns, 3x rows and 3x columns
        # return a 9x9 list
        self.shuffle_numbers()
        self.shuffle_rows()
        self.shuffle_columns()
        self.shuffle_3x_rows()
        self.shuffle_3x_columns()