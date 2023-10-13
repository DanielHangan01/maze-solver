from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None, start_x = 0,start_y = 0):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._start_x = start_x
        self._start_y = start_y

        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(start_x, start_y)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.00005)

    def _break_entrance_and_exit(self):
        if self._start_x != 0 and self._start_x != self._num_cols - 1 and self._start_y != 0 and self._start_y != self._num_rows - 1:
            raise Exception("Entrance is supposed to be on one of the edges")
        entrance = self._cells[self._start_x][self._start_y]
        exit = self._cells[self._num_cols - 1][self._num_rows - 1]
        if self._start_x == 0 and self._start_y == 0:
            entrance.has_top_wall = False
        elif self._start_x == 0:
            entrance.has_left_wall = False
        elif self._start_y == 0:
            entrance.has_right_wall = False
        else:
            entrance.has_bottom_wall = False
        self._draw_cell(self._start_x, self._start_y)
        exit.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = []
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append((i, j + 1))
            if len(neighbors) == 0:
                self._draw_cell(i, j)
                return
            dir = random.randrange(len(neighbors))
            next = neighbors[dir]
            #left
            if next[0] == i - 1:
                self._cells[i - 1][j].has_right_wall = False
                self._cells[i][j].has_left_wall = False
            #right
            elif next[0] == i + 1:
                self._cells[i + 1][j].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            #up
            elif next[1] == j - 1:
                self._cells[i][j - 1].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            #down
            else:
                self._cells[i][j + 1].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            #visit next cell
            self._break_walls_r(next[0], next[1])
                        
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(self._start_x, self._start_y)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        #left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        #right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        #up
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        #down
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        
        return False
            