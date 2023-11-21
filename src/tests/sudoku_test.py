import unittest
from sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku(([[0,0,0,0,0,0,1,0,0],
                                [0,0,3,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [2,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0]]))
        
    def test_check_number_row(self):
        self.assertEqual(self.sudoku.check_number(0,0,1), True)

    def test_check_number_column(self):
        self.assertEqual(self.sudoku.check_number(0,0,2), True)

    def test_check_number_box(self):
        self.assertEqual(self.sudoku.check_number(0,0,3), True)

    def test_check_number_valid(self):
        self.assertEqual(self.sudoku.check_number(0,0,4), False)