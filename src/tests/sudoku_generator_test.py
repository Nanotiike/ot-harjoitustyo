import unittest
from sudoku_generator import generate_sudoku
from sudoku import Sudoku

class TestSudokuGenerator(unittest.TestCase):
    def setUp(self):
        self.sudoku = generate_sudoku()

    def test_generate_sudoku_correct_size(self):
        self.assertEqual(len(self.sudoku.board), 9)
        self.assertEqual(len(self.sudoku.board[0]), 9)
    
    """def test_generate_sudoku_shuffle_numbers(self):
        self.sudoku.shuffle_numbers()
        self.assertNotEqual(self.sudoku.board, [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                                                [5, 6, 4, 8, 9, 7, 2, 3, 1],
                                                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                                                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                                                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                                                [9, 7, 8, 3, 1, 2, 6, 4, 5]])
        
    def test_generate_sudoku_shuffle_rows(self):
        self.sudoku.shuffle_rows()
        self.assertNotEqual(self.sudoku.board, [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                                                [5, 6, 4, 8, 9, 7, 2, 3, 1],
                                                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                                                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                                                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                                                [9, 7, 8, 3, 1, 2, 6, 4, 5]])
        
    def test_generate_sudoku_shuffle_columns(self):
        self.sudoku.shuffle_columns()
        self.assertNotEqual(self.sudoku.board, [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                                                [5, 6, 4, 8, 9, 7, 2, 3, 1],
                                                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                                                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                                                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                                                [9, 7, 8, 3, 1, 2, 6, 4, 5]])
        
    def test_generate_sudoku_shuffle_3x_rows(self):
        self.sudoku.shuffle_3x_rows()
        self.assertNotEqual(self.sudoku.board, [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                                                [5, 6, 4, 8, 9, 7, 2, 3, 1],
                                                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                                                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                                                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                                                [9, 7, 8, 3, 1, 2, 6, 4, 5]])
        
    def test_generate_sudoku_shuffle_3x_columns(self):
        self.sudoku.shuffle_3x_columns()
        self.assertNotEqual(self.sudoku.board, [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                                                [5, 6, 4, 8, 9, 7, 2, 3, 1],
                                                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                                                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                                                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                                                [9, 7, 8, 3, 1, 2, 6, 4, 5]])"""
        
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