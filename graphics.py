from tkinter import *
import time
import random
import copy

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("dsav")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

        self.__width = width
        self.__height = height
    
    def get_root(self):
        return self__root

    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def get_canvas(self):
        return self.__canvas

    def get_root(self):
        return self.__root

    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
        print("window closed")

    def close(self):
        self.__running = False

    def draw_rectangles(self):
        self.__canvas.delete("all")

        x0 = 0
        for rec in self.recs:
            rec.draw(self.__canvas, x0)
            x0 += self.recwidth



class Rectangle():
    def __init__(self, x, y, width, screenheight, color, value, max_len):
        topmargin = 10
        self.height = value * ((screenheight - topmargin) // max_len) 
        # rec start x (left of screen)
        self.x0 = x
        # rec start y (bottom of screen)
        self.__y0 = y
        # rec end x
        self.__x1 = x + width
        # rec end y (TODO: should be calculate on draw)
        self.__y1 = y - self.height
        self.__color = color
        self.value = value
        self.max_len = max_len
        self.height = self.height

    def __repr__(self):
        return f"{self.x0}, {self.__y1}, {self.value}"

    def draw(self, canvas, startx=None, color=None):
        if startx is None:
            startx = self.x0
        if color is None:
            color = self.__color
        # y1 should be calculated dynamically
        self.__y1 = self.__y0 - self.height
        endx = startx + 10;
        self.x0 = startx
        canvas.create_rectangle(
            startx, self.__y0, endx, self.__y1, fill=color
        )
