import sys

MIN_INT = -sys.maxsize - 1

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    arr = []
    max = MIN_INT

    for i in range(m + 1):
        arr.append([0] * (n + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                if arr[i][j] > max:
                    max = arr[i][j]
                else:
                    arr[i][j] = 0
    
    return max

print lcs("abcdxyz", "xyzabcd")