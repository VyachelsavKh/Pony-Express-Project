from tkinter import *
from math import *
import time

SIZE_X = 1450
SIZE_Y = SIZE_X/16*9

r = Tk()

#r.wm_attributes('-topmost', 1)
canv = Canvas(r, width=SIZE_X, height=SIZE_Y, bg="white")
canv.pack()

def triangle(x, y, l, fill = "black"):
    y = SIZE_Y - y
    canv.create_polygon([x, y], [x + l, y], [x+l/2,y+l*sin(pi/3)], fill = fill)
    r.update()

def serp(x, y, l, count):
    canv.create_polygon([x, SIZE_Y-y], [x + l, SIZE_Y-y], [x + l / 2, SIZE_Y - y - l * sin(pi / 3)])
    r.update()

    serp_(x, y, l, count)

def serp_(x, y, l, count):
    print(count)
    if count:
        triangle(x+l/4, y + l / 2 * sin(pi/3), l/2,"white")
        count -= 1
        serp_(x, y, l/2, count)
        serp_(x+l/4, y + l / 2 * sin(pi/3), l/2, count)
        serp_(x+l/2, y, l/2, count)

def line(x1, y1, x2, y2, fill = "black", width = 1):
    y1 = SIZE_Y - y1
    y2 = SIZE_Y - y2

    canv.create_line(x1, y1, x2, y2, fill = fill, width = width)
    r.update()

def koch(x, y, l, count, angle = 60):
    line(x, y, x+l, y)

    angle = angle / 180 * pi

    koch_(x, y, l, 0, count, angle)

def koch_(x, y, l, angle, count, angle2):
    print(count)
    if count:
        line(x + l / 3 * cos(angle),
             y + l / 3 * sin(angle),
             x + 2 * l / 3 * cos(angle),
             y + 2 * l / 3 * sin(angle),
             "white", 3)

        line(x + l / 3 * cos(angle),
             y + l / 3 * sin(angle),
             x + l / 3 * cos(angle) + l / 6 / cos(angle2) * cos(angle + angle2),
             y + l / 3 * sin(angle) + l / 6 / cos(angle2) * sin(angle + angle2))

        line(x + 2 * l / 3 * cos(angle),
             y + 2 * l / 3 * sin(angle),
             x + l / 3 * cos(angle) + l / 6 / cos(angle2) * cos(angle + angle2),
             y + l / 3 * sin(angle) + l / 6 / cos(angle2) * sin(angle + angle2))

        count -= 1

        koch_(x, y, l/3, angle, count, angle2)
        koch_(x + 2 * l / 3 * cos(angle), y + 2 * l / 3 * sin(angle), l/3, angle, count, angle2)

        koch_(x + l / 3 * cos(angle),
              y + l / 3 * sin(angle),
              l / 6 / cos(angle2), angle + angle2, count, angle2)
        koch_(x + l / 3 * cos(angle) + l / 6 / cos(angle2) * cos(angle + angle2),
             y + l / 3 * sin(angle) + l / 6 / cos(angle2) * sin(angle + angle2),
              l / 6 / cos(angle2), angle - angle2, count, angle2)

if __name__ == "__main__":
    serp(20, 20, 900, 7)
    #koch(20, 20, SIZE_X-2*20, 4, angle = 71)

    r.mainloop()