def ceil_index(arr, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r


def lis(arr):
    size = len(arr)

    tail_table = [0 for _ in range(size + 1)]
    l = 0

    tail_table[0] = arr[0]
    l = 1

    for i in range(1, size):
        if arr[i] < tail_table[0]:
            tail_table[0] = arr[i]
        elif arr[i] > tail_table[l - 1]:
            tail_table[l] = arr[i]
            l += 1
        else:
            tail_table[ceil_index(tail_table, -1, l - 1, arr[i])] = arr[i]

    return l


print lis([2, 5, 3, 7, 11, 8, 10, 13, 6])