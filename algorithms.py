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
    time.sleep(1)
    sorted = list

    while True:
        is_sorted = True
        for i in range(1, len(sorted)):
            window.redraw()
            # usleep(1000)
            time.sleep(0.001)
            window.draw_rectangles(sorted)
            if sorted[i - 1][0] > sorted[i][0]:
                sorted[i - 1] = (sorted[i - 1][0], "red")
                sorted[i] = (sorted[i][0], "red")
                window.redraw()
                time.sleep(0.001)
                # usleep(1000)
                window.draw_rectangles(sorted)
                temp = sorted[i]
                sorted[i] = (sorted[i - 1][0], "white")
                sorted[i - 1] = (temp[0], "white")
                is_sorted = False
        if is_sorted:
            break
    for i in range(0, len(sorted)):
        window.redraw()
        sorted[i] = (sorted[i][0], "green")
        time.sleep(0.001)
        window.draw_rectangles(sorted)
    return sorted
