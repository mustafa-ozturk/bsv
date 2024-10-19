from graphics import Window, Rectangle
from algorithms import bubble_sort
import random

def main():
    WIDTH = 1280
    HEIGHT = 720
    window = Window(WIDTH, HEIGHT)
    # self.__canvas.create_rectangle(10, self.__height, 20, 100, fill="white")


    width = 10
    spacing = 10
    max_len = WIDTH //(width + spacing);

    list = []
    """
    for i in range(max_len):
        list.append(random.randrange(1, 15))
    """

    for i in range(max_len, 0, -1):
       list.append(i)
    random.shuffle(list)


    bubble_sort(list, window)
    window.wait_for_close()
    pass

main()
