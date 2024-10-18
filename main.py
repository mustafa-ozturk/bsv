from graphics import Window, Rectangle
from algorithms import bubble_sort

def main():
    WIDTH = 800
    HEIGHT = 800
    window = Window(WIDTH, HEIGHT)
    # self.__canvas.create_rectangle(10, self.__height, 20, 100, fill="white")
    list = [10, 9, 12, 8,7, 7, 6, 15, 15, 5, 3, 2, 7, 6, 6, 5, 5, 4, 13, 3, 2, 1]
    bubble_sort(list, window)
    window.wait_for_close()
    pass

main()
