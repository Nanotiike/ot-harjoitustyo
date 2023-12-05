import unittest
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [4, 5, 6, 7, 8, 9, 1, 2, 3],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [2, 3, 1, 5, 6, 4, 8, 9, 7],
                            [5, 6, 4, 8, 9, 7, 2, 3, 1],
                            [8, 9, 7, 2, 3, 1, 5, 6, 4],
                            [3, 1, 2, 6, 4, 5, 9, 7, 8],
                            [6, 4, 5, 9, 7, 8, 3, 1, 2],
                            [9, 7, 8, 3, 1, 2, 6, 4, 5]])

    def test_check_number_row(self):
        self.assertEqual(self.sudoku.check_number(0, 0, 1), True)

    def test_check_number_column(self):
        self.assertEqual(self.sudoku.check_number(0, 0, 2), True)

    def test_check_number_box(self):
        self.assertEqual(self.sudoku.check_number(0, 0, 3), True)

    def test_create_player_board_clues(self):
        clues = 0
        for i in range(9):
            for j in range(9):
                if self.sudoku.player_board[i][j] != 0:
                    clues += 1
        self.assertEqual(clues, 17)

    def test_make_move(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.player_board[i][j] == 0:
                    self.assertEqual(self.sudoku.make_move(i, j, self.sudoku.board[i][j]), 0)
                    break
                else:
                    self.assertEqual(self.sudoku.make_move(i, j, 3), 2)
            for j in range(9):
                if self.sudoku.player_board[i][j] == 0:    
                    self.assertEqual(self.sudoku.make_move(i, j, self.sudoku.board[i][j]+1), 1)
                    break
                else:
                    self.assertEqual(self.sudoku.make_move(i, j, 3), 2)
            break
        
