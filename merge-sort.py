def merge(x, y):
    p1 = p2 = 0
    result = []

    while p1 < len(x) and p2 < len(y):
        if x[p1] < y[p2]:
            result.append(x[p1])
            p1 += 1
        else:
            result.append(y[p2])
            p2 += 1

    result += x[p1:] + y[p2:]
    return result


def merge1(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2

    print len(L)
    for i in range(n1):
        L[i] = arr[left + i]
    for i in range(n2):
        R[i] = arr[mid + i + 1]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] > R[i]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return sorted(arr)

    mid = len(arr) / 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge_sort_bottom_up(arr):
    n = len(arr)
    current_size = 1

    # Outer loop for traversing each sub array of current_size
    while current_size < n - 1:
        left = 0

        # Inner loop for merge call in a sub array
        # Each complete iteration sorts the iterating sub array
        while left < n - 1:
            mid = left + current_size - 1
            right = ((2 * current_size + left - 1, n - 1)[2 * current_size + left - 1 > n - 1])

            # merge for each sub array
            merge1(arr, left, mid, right)
            left = left + current_size * 2
        
        current_size *= 2

    return arr

print merge_sort([12, 32, 34, 65, 6, 2, 6, 2, 6])
print merge_sort_bottom_up([12, 32, 34, 65, 6, 2, 6, 2, 6])
