def spiralOrder(self, matrix):
    results = []
    m = len(matrix)

    if m == 0:
        return []

    n = len(matrix[0])

    k, l = 0, 0
    while k < m and l < n:
        for i in range(l, n):
            results.append(matrix[k][i])
        k += 1

        for i in range(k, m):
            results.append(matrix[i][n - 1])
        n -= 1

        if k < m:
            for i in range(n - 1, l - 1, -1):
                results.append(matrix[m - 1][i])
            m -= 1

        if l < n:
            for i in range(m - 1, k - 1, -1):
                results.append(matrix[i][l])
            l += 1

    return results
