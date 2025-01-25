from cell import Cell
from window import Line, Point, Window


def main():
    point_one = Point(100, 400)
    point_two = Point(400, 100)
    win = Window(800, 600)
    my_cell = Cell(win)

    # my_cell.has_top_wall = False
    # my_cell.has_left_wall = False

    my_cell.draw(point_one.x, point_two.x, point_two.y, point_one.y)

    win.wait_for_close()


main()
