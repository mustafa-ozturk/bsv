from graphics import Window

def main():
    WIDTH = 800
    HEIGHT = 800
    window = Window(WIDTH, HEIGHT)
    window.draw_rectangle()
    window.wait_for_close()
    pass

main()
