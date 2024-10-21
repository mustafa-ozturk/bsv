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

    def get_canvas(self):
        return self.__canvas

    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
        print("window closed")

    def close(self):
        self.__running = False

    def draw_rectangles(self, list):
        self.__canvas.delete("all")
        width = 10
        spacing = 10
        max_len = self.__width //(width + spacing);

        recs = []

        x0 = 0
        for num in list:
            recs.append(Rectangle(x0 + spacing, self.__height, width, num * (self.__height // max_len), "white", num));
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
