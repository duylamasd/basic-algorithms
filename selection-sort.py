def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        min_value = arr[i]

        for j in range(i + 1, n):
            if arr[j] < min_value:
                min_idx = j
                min_value = arr[j]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print arr


selection_sort([12, 32, 34, 65, 6, 2, 6, 2, 6])
