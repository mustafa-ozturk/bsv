from graphics import Window, Rectangle
from algorithms import bubble_sort
import random

def main():
    WIDTH = 500
    HEIGHT = 500
    window = Window(WIDTH, HEIGHT)
    # self.__canvas.create_rectangle(10, self.__height, 20, 100, fill="white")

    """
    for i in range(max_len):
        list.append(random.randrange(1, 15))
    """

    # 1. create a reverse sorted list
    #   - shuffle the list to randomize
    # 2. call bubble_sort(random_list)
    #   - draw_rectangles

    random_list = []
    width = 10
    spacing = 10
    max_len = WIDTH //(width + spacing);

    for i in range(max_len, 0, -1):
        random_list.append((i, "white"))
    random.shuffle(random_list)

    bubble_sort(random_list, window)

    window.wait_for_close()
    return

main()
