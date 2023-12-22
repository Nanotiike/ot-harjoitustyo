import unittest
from sudoku_generator import Generate_sudoku
from sudoku import Sudoku

class TestSudokuGenerator(unittest.TestCase):
    def setUp(self):
        self.sudoku = Generate_sudoku()

    def test_generate_sudoku_correct_size(self):
        self.assertEqual(len(self.sudoku.board), 9)
        self.assertEqual(len(self.sudoku.board[0]), 9)
    
    def test_generate_sudoku_shuffle_numbers(self):
        self.sudoku.shuffle_numbers()
        self.sudoku_player = Sudoku(self.sudoku.board)
        result = True
        for i in range(9):
            for j in range(9):
                if self.sudoku_player.check_number(i, j, self.sudoku_player.board[i][j]) == False:
                    result = False
                    break
        self.assertEqual(result, True)
        
    def test_generate_sudoku_shuffle_rows(self):
        self.sudoku.shuffle_rows()
        self.sudoku_player = Sudoku(self.sudoku.board)
        result = True
        for i in range(9):
            for j in range(9):
                if self.sudoku_player.check_number(i, j, self.sudoku_player.board[i][j]) == False:
                    result = False
                    break
        self.assertEqual(result, True)
        
    def test_generate_sudoku_shuffle_columns(self):
        self.sudoku.shuffle_columns()
        self.sudoku_player = Sudoku(self.sudoku.board)
        result = True
        for i in range(9):
            for j in range(9):
                if self.sudoku_player.check_number(i, j, self.sudoku_player.board[i][j]) == False:
                    result = False
                    break
        self.assertEqual(result, True)
        
    def test_generate_sudoku_shuffle_3x_rows(self):
        self.sudoku.shuffle_3x_rows()
        self.sudoku_player = Sudoku(self.sudoku.board)
        result = True
        for i in range(9):
            for j in range(9):
                if self.sudoku_player.check_number(i, j, self.sudoku_player.board[i][j]) == False:
                    result = False
                    break
        self.assertEqual(result, True)
        
    def test_generate_sudoku_shuffle_3x_columns(self):
        self.sudoku.shuffle_3x_columns()
        self.sudoku_player = Sudoku(self.sudoku.board)
        result = True
        for i in range(9):
            for j in range(9):
                if self.sudoku_player.check_number(i, j, self.sudoku_player.board[i][j]) == False:
                    result = False
                    break
        self.assertEqual(result, True)
        
    def test_validate_sudoku(self):
        self.sudoku.shuffle_numbers()
        self.sudoku.shuffle_rows()
        self.sudoku.shuffle_columns()
        self.sudoku.shuffle_3x_rows()
        self.sudoku.shuffle_3x_columns()
        self.sudoku_player = Sudoku(self.sudoku.board)
        result = True
        for i in range(9):
            for j in range(9):
                if self.sudoku_player.check_number(i, j, self.sudoku_player.board[i][j]) == False:
                    result = False
                    break
        self.assertEqual(result, True)