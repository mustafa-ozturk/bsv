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
        self.button = Button(self.__root, text="next iteration", command=self.test_pp1)
        self.button.place(x = 10, y = 10)

        self.pause = True
        self.list = []

        width = 10
        max_len = self.__width // width;

        for i in range(max_len, 0, -1):
            self.list.append((i, "white"))
        random.shuffle(self.list)

        self.is_sorted = False

        self.recwidth = 10
        # spacing = 10
        max_len = self.__width // self.recwidth;

        self.recs = []

        x0 = 0
        for num, color in self.list:
            print(num, color)
            self.recs.append(Rectangle(x0, self.__height, self.recwidth, self.__height, color, num, max_len));
            x0 += self.recwidth
        # draw every rectangle white
        for i in range(0, len(self.recs)):
            self.draw_rectangle(i, "white")

    def test_pp(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False

        # draw every rectangle white
        for i in range(0, len(self.list)):
            self.draw_rectangle(i, "white")

        # draw last recantle white and current one white
        for i in range(0, len(self.list)):
            time.sleep(0.5)
            if i > 0:
                self.draw_rectangle(i - 1, "white")
            self.draw_rectangle(i, "red")
            self.redraw()

    # testing pp logic with bubble sort
    # highlight i - 1 and i as read, and i - 2 as white if it exists
    def test_pp1(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False

        str = "current values: "
        for rec in self.recs:
            str += f"{rec.value}" + ' ,'

        print('>>>>', str)


        # draw last recantle white and current one white
        for i in range(1, len(self.recs)):
            time.sleep(0.001)
            if i > 1:
                self.draw_rectangle(i - 2, "white")
            self.draw_rectangle(i - 1, "red")
            self.draw_rectangle(i, "red")
            self.redraw()
            # bubble sort
            if self.recs[i - 1].value > self.recs[i].value:
                # swapping rectangles
                self.recs[i - 1], self.recs[i] = self.recs[i], self.recs[i - 1],
                time.sleep(0.01)
                self.draw_rectangles()

    def draw_rectangle(self, index, color):
        self.recs[index].draw(self.get_canvas(), color=color);

    def play_pause(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False

        self.draw_rectangles()
        is_sorted = True
        for i in range(1, len(self.list)):
            self.redraw()
            time.sleep(0.001)
            if self.list[i - 1][0] > self.list[i][0]:
                temp = self.list[i]
                self.list[i] = (self.list[i - 1][0], "white")
                self.list[i - 1] = (temp[0], "white")

                time.sleep(0.5)
                # TODO: should modify rectangles directly
                temprec = self.recs[i]
                self.recs[i] = self.recs[i - 1]
                self.recs[i - 1] = temprec

                self.draw_rectangle(i - 1, "red")
                self.draw_rectangle(i, "red")
                self.redraw()
                # self.draw_rectangles()
                is_sorted = False

        if is_sorted:
            for i in range(0, len(self.list)):
                self.redraw()
                self.list[i] = (self.list[i][0], "green")
                time.sleep(0.001)
                self.draw_rectangles()



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

    # TODO: this should only run a for loop on a list of rectangles
    # and call draw on each
    def draw_rectangles(self):
        self.__canvas.delete("all")

        x0 = 0
        for rec in self.recs:
            rec.draw(self.__canvas, x0)
            x0 += self.recwidth



class Rectangle():
    def __init__(self, x, y, width, screenheight, color, value, max_len):
        self.height = value * (screenheight // max_len)
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
