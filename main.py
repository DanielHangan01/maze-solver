from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(0, 0), Point(100, 200))
    line2 = Line(Point(300, 300), Point(500, 500))
    win.draw_line(line1, "red")
    win.draw_line(line2)
    win.wait_for_close()

main()