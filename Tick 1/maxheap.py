import math


def heapify(x):
    for i in range(math.floor(len(x)/2) - 1, -1, -1):
        left_child = x[2 * i + 1]
        right_child = x[2 * i + 2] if len(x) > 2 * i + 2 else x[2 * i + 1]
        while x[i] < left_child or x[i] < right_child:
            if left_child >= right_child:
                temp = x[i]
                x[i] = left_child
                x[2 * i + 1] = temp
                i = 2 * i + 1
            else:
                temp = x[i]
                x[i] = right_child
                x[2 * i + 2] = temp
                i = 2 * i + 2
            if len(x) > 2 * i + 1:
                left_child = x[2 * i + 1]
                right_child = x[2 * i + 2] if len(x) > 2 * i + 2 else x[2 * i + 1]
            else:
                break


def push(x, e):
    x.append(e)
    i = len(x) - 1
    while i != 0:
        if (i-1) % 2 == 0:
            if x[int((i-1)/2)] < x[i]:
                temp = x[i]
                x[i] = x[int((i-1)/2)]
                x[int((i-1)/2)] = temp
                i = int((i-1)/2)
            else:
                break
        else:
            if x[int((i-2)/2)] < x[i]:
                temp = x[i]
                x[i] = x[int((i-2)/2)]
                x[int((i-2)/2)] = temp
                i = int((i-2)/2)
            else:
                break


def popmax(x):
    if len(x) == 0:
        raise IndexError
    to_return = x[0]
    x[0] = x[-1]
    x.pop()
    i = 0
    while len(x) > (2 * i + 1) or len(x) > (2 * i + 2):
        if not (len(x) > (2 * i + 2)):
            if x[2 * i + 1] > x[i]:
                x[i], x[2 * i + 1] = x[2 * i + 1], x[i]
                i = 2 * i + 1
            else:
                break
        else:
            if x[2 * i + 1] > x[i] or x[2 * i + 2] > x[i]:
                if x[2 * i + 1] > x[2 * i + 2]:
                    x[i], x[2 * i + 1] = x[2 * i + 1], x[i]
                    i = 2 * i + 1
                else:
                    x[i], x[2 * i + 2] = x[2 * i + 2], x[i]
                    i = 2 * i + 2
    return to_return
