from cell import Cell
from maze import Maze
from window import Line, Point, Window


def main():
    point_zero = Point(0, 0)

    # top-left corner and bottom-right corner to make one square
    # point_one = Point(100, 200)
    # point_two = Point(200, 100)

    # point_three = Point(150, 100)
    # point_four = Point(200, 50)

    win = Window(800, 600)
    # first_cell = Cell(win)
    # second_cell = Cell(win)

    # my_line = Line(point_zero, point_four)
    # win.draw_line(my_line, "red")

    # first_cell.draw(point_one.x, point_two.x, point_two.y, point_one.y)
    # second_cell.draw(point_three.x, point_four.x, point_four.y, point_three.y)

    # first_cell.draw_move(second_cell)

    maze = Maze(50, 50, 10, 10, 25, 25, win)

    win.wait_for_close()


main()
