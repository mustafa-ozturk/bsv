import time

# usleep(100) sleeps for 100 microsecons
# 100 seems to be the limit
usleep = lambda x: time.sleep(x/1000000.0)

"""
repeat until sorted:
    if i > i + 1
        swap them
"""
def bubble_sort(list, window):
    sorted = list
    window.draw_rectangles(list)
    while True:
        is_sorted = True
        for i in range(1, len(sorted)):
            window.redraw()
            usleep(100)
            window.clear()
            window.draw_rectangles(sorted)
            # window.highlight_pointer(i, "blue")
            if sorted[i - 1] > sorted[i]:
                # window.highlight_bar(i - 1, "red")
                # window.highlight_bar(i, "red")
                # window.draw_bars(sorted)
                temp = sorted[i]
                sorted[i] = sorted[i - 1]
                sorted[i - 1] = temp
                is_sorted = False
                # window.highlight_bar(i - 1, "white")
                # window.highlight_bar(i, "white")
                # window.draw_bars(sorted)
        if is_sorted:
            break
    # window.highlight_all("green")
    return sorted
