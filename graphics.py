from tkinter import Tk, BOTH, Canvas

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

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
        print("window closed")

    def close(self):
        self.__running = False

    def draw_rectangle(self, rectangle, fill_color):
        rectangle.draw(self.__canvas, fill_color)
        # self.__canvas.create_rectangle(10, self.__height, 20, 100, fill="white")

    def draw_rectangles(self, list):
        recs = []
        curr_x = 10
        for num in list:
            # height should be based on list number
            recs.append(Rectangle(curr_x, self.__height, 20, num * 50))
            curr_x += 30

        for rec in recs:
            self.draw_rectangle(rec, "white")

    def clear(self):
        self.__canvas.delete("all")

class Rectangle():
    def __init__(self, x, y, width, height):
        self.__x0 = x
        self.__y0 = y
        self.__x1 = x + width
        self.__y1 = y - height

    def draw(self, canvas, fill_color):
        print("y0:", self.__y0, "y1:", self.__y1)
        canvas.create_rectangle(
            self.__x0, self.__y0, self.__x1, self.__y1, fill=fill_color
        )
