def binary_search(arr, x, low, high):
    """
    Binary search algorithm
    """
    if low > high:
        return -1

    mid = low + (high - low) / 2

    if x == arr[mid]:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, low, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, high)


def iterative_binary_search(arr, x):
    """
    The iterative binary search
    """
    low = 0
    high = len(arr)

    mid = low + (high - low) / 2

    while x != arr[mid] and low <= high:
        if x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

        mid = low + (high - low) / 2

    if low > high:
        return -1

    return mid


print binary_search([1, 3, 4, 5], 4, 0, 3)
print iterative_binary_search([1, 3, 4, 5], 4)
