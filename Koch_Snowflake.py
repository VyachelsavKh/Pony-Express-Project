from tkinter import *
from math import *
import time

class Koch_Snowflake:
    def __init__(self, size_x = 1000, aspect_ratio = 16/9):
        self.size_x = size_x
        self.size_y = size_x / aspect_ratio
        self.r = Tk()
        # r.wm_attributes('-topmost', 1)
        self.canv = Canvas(self.r, width=size_x, height=size_x / aspect_ratio, bg="white")
        self.canv.pack()

    def __line(self, x1, y1, x2, y2, fill="black", width=1):
        y1 = self.size_y - y1
        y2 = self.size_y - y2

        self.canv.create_line(x1, y1, x2, y2, fill=fill, width=width)
        self.r.update()

    def __koch(self, x, y, l, angle, count, angle2):
        print(count)
        #time.sleep(1)
        if count:
            self.__line(x + l / 3 * cos(angle),
                 y + l / 3 * sin(angle),
                 x + 2 * l / 3 * cos(angle),
                 y + 2 * l / 3 * sin(angle),
                 "white", 3)

            self.__line(x + l / 3 * cos(angle),
                 y + l / 3 * sin(angle),
                 x + l / 3 * cos(angle) + l / 6 / cos(angle2) * cos(angle + angle2),
                 y + l / 3 * sin(angle) + l / 6 / cos(angle2) * sin(angle + angle2))

            self.__line(x + 2 * l / 3 * cos(angle),
                 y + 2 * l / 3 * sin(angle),
                 x + l / 3 * cos(angle) + l / 6 / cos(angle2) * cos(angle + angle2),
                 y + l / 3 * sin(angle) + l / 6 / cos(angle2) * sin(angle + angle2))

            count -= 1

            self.__koch(x, y, l / 3, angle, count, angle2)
            self.__koch(x + 2 * l / 3 * cos(angle), y + 2 * l / 3 * sin(angle), l / 3, angle, count, angle2)

            self.__koch(x + l / 3 * cos(angle),
                  y + l / 3 * sin(angle),
                  l / 6 / cos(angle2), angle + angle2, count, angle2)
            self.__koch(x + l / 3 * cos(angle) + l / 6 / cos(angle2) * cos(angle + angle2),
                  y + l / 3 * sin(angle) + l / 6 / cos(angle2) * sin(angle + angle2),
                  l / 6 / cos(angle2), angle - angle2, count, angle2)

    def print(self, count, angle=60):

        x = 20
        y = 20
        l = self.size_x - 2*x

        self.__line(x, y, x + l, y)

        angle = angle / 180 * pi

        self.__koch(x, y, l, 0, count, angle)

        self.r.mainloop()

Snowflake = Koch_Snowflake(1400)

if __name__ == "__main__":
    Snowflake.print(6, 60)
    