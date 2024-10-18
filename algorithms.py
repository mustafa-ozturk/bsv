
"""
repeat until sorted:
    if i > i + 1
        swap them
"""
def bubble_sort(list):
    sorted = list
    while True:
        is_sorted = True
        for i in range(1, len(sorted)):
            if sorted[i - 1] > sorted[i]:
                temp = sorted[i]
                sorted[i] = sorted[i - 1]
                sorted[i - 1] = temp
                is_sorted = False
        if is_sorted:
            break
    return sorted
