import time
from cell import Cell
from window import Point


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        point_one = Point(
            self.x1 + (i * self.cell_size_x), self.y1 + (j * self.cell_size_y)
        )
        point_two = Point(
            self.x1 + ((i + 1) * self.cell_size_x),
            self.y1 + ((j + 1) * self.cell_size_y),
        )

        self._cells[i][j].draw(point_one.x, point_two.x, point_two.y, point_one.y)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.num_cols - 1][self.num_rows - 1]

        entrance_cell.has_bottom_wall = False
        self._draw_cell(0, 0)

        exit_cell.has_top_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
