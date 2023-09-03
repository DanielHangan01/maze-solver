from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(0, 0, 300, 300)
    cell1.draw(600, 600, 790, 790)
    win.wait_for_close()

main()