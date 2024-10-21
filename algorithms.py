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

    while True:
        is_sorted = True
        for i in range(1, len(sorted)):
            window.redraw()
            usleep(100)
            window.draw_rectangles(sorted)
            if sorted[i - 1] > sorted[i]:
                temp = sorted[i]
                sorted[i] = sorted[i - 1]
                sorted[i - 1] = temp
                is_sorted = False
        if is_sorted:
            break
    return sorted
