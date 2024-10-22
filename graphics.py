from tkinter import *
import time
import random

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

        # Create the main button
        self.button = Button(self.__root, text="next iteration", command=self.play_pause)
        self.button.place(x = 10, y = 10)

        self.pause = True
        self.list = []

        width = 10
        spacing = 10
        max_len = self.__width //(width + spacing);

        for i in range(max_len, 0, -1):
            self.list.append((i, "white"))
        random.shuffle(self.list)

        self.is_sorted = False


    def play_pause(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False

        is_sorted = True
        for i in range(1, len(self.list)):
            self.redraw()
            time.sleep(0.001)
            self.draw_rectangles()
            if self.list[i - 1][0] > self.list[i][0]:
                temp = self.list[i]
                self.list[i] = (self.list[i - 1][0], "white")
                self.list[i - 1] = (temp[0], "white")
                self.redraw()
                time.sleep(0.001)
                self.draw_rectangles()
                is_sorted = False

        if is_sorted:
            for i in range(0, len(self.list)):
                self.redraw()
                self.list[i] = (self.list[i][0], "green")
                time.sleep(0.001)
                self.draw_rectangles()

            """
            for i in range(1, len(self.list)):
                self.redraw()
                time.sleep(0.001)
                self.draw_rectangles(list)
                if self.list[i - 1][0] > self.list[i][0]:
                    self.list[i - 1] = (self.list[i - 1][0], "red")
                    self.list[i] = (self.list[i][0], "red")
                    self.redraw()
                    time.sleep(0.001)
                    self.draw_rectangles(sorted)
                    temp = self.list[i]
                    self.list[i] = (self.list[i - 1][0], "white")
                    self.list[i - 1] = (temp[0], "white")
                    is_sorted = False
                if is_sorted:
                    break
            """



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
        width = 10
        spacing = 10
        max_len = self.__width //(width + spacing);

        recs = []

        x0 = 0
        for num, color in self.list:
            print(num, color)
            recs.append(Rectangle(x0 + spacing, self.__height, width, num * (self.__height // max_len), color, num));
            x0 += width + spacing


        for rec in recs:
            rec.draw(self.__canvas)



class Rectangle():
    def __init__(self, x, y, width, height, color, value):
        self.__x0 = x
        self.__y0 = y
        self.__x1 = x + width
        self.__y1 = y - height
        self.__color = color
        self.value = value

    def __repr__(self):
        return f"{self.__x0}, {self.__y1}, {self.value}"

    def draw(self, canvas):
        canvas.create_rectangle(
            self.__x0, self.__y0, self.__x1, self.__y1, fill=self.__color
        )
