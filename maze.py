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

    def _create_cells(self):
        self._cells = [[] for col in range(self.num_rows)]
        for row_idx, i in enumerate(range(self.num_rows)):
            for col_idx, j in enumerate(range(self.num_cols)):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        point_one = Point(
            self.x1 + (i * self.cell_size_x), self.y1 + (j * self.cell_size_y)
        )
        point_two = Point(
            self.x1 + ((i + 1) * self.cell_size_x),
            self.y1 + ((j + 1) * self.cell_size_y),
        )

        cell = Cell(self.win)
        self._cells[i].append(cell)
        cell.draw(point_one.x, point_two.x, point_two.y, point_one.y)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.03)
