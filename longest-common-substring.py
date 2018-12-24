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


def print_lcs(arr):
    n = len(arr)
    s = arr[0]
    l = len(s)

    res = ""

    for i in range(l):
        for j in range(i + 1, l + 1):
            stem = s[i:j]
            k = 1
            while k < n:
                if stem not in arr[k]:
                    break
                k += 1

            if k == n and len(res) < len(stem):
                res = stem

    return res


print lcs("abcdxyz", "xyzabcd")
print print_lcs(["ca", "a"])
