class Stack:
    """
    This class represents a stack
    """

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return not self.stack


def partition(arr, l, h):
    i = l - 1
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quick_sort(arr, l, h):
    stack = Stack()

    stack.push(l)
    stack.push(h)

    while not stack.empty():
        h = stack.pop()
        l = stack.pop()

        p = partition(arr, l, h)

        if p - 1 > l:
            stack.push(l)
            stack.push(p - 1)

        if p + 1 < h:
            stack.push(p + 1)
            stack.push(h)

    print arr


arr = [12, 32, 34, 65, 6, 2, 6, 2, 6]
quick_sort(arr, 0, len(arr) - 1)
