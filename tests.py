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
        #self.assertEqual(m1._cells[5][3]._x1, 210)
        #self.assertEqual(m1._cells[5][3]._x2, 250)
        #self.assertEqual(m1._cells[8][9]._y1, 220)
        #self.assertEqual(m1._cells[8][9]._y2, 380)

        m1._win.wait_and_close()

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

        m1._win.wait_and_close()

if __name__ == "__main__":
    unittest.main()