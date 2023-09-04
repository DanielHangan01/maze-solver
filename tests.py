import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_coordinates(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(200, 200, num_rows, num_cols, 10, 20, win = Window(800, 600))
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        self.assertEqual(m1._cells[5][3]._x1, 210)
        self.assertEqual(m1._cells[5][3]._x2, 250)
        self.assertEqual(m1._cells[8][9]._y1, 220)
        self.assertEqual(m1._cells[8][9]._y2, 380)

if __name__ == "__main__":
    unittest.main()