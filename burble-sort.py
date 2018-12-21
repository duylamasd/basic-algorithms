def burble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print arr


burble_sort([10, 1, 2, 11])
