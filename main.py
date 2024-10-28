from tkinter import Button
from tkinter import Tk
from graphics import Window, Rectangle
from algorithms import bubble_sort
import random
from bubblesort import BubbleSort


def main():
    WIDTH = 900
    HEIGHT = 720
    window = Window(WIDTH, HEIGHT)
    bubbleSort = BubbleSort(window)
    bubbleSort.draw()
    window.wait_for_close()
    return

main()
