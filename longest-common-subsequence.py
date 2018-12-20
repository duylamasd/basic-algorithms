def recursive_lcs(str1, str2, m, n):
    if m == 0 or n == 0:
        return 0
    if str1[m - 1] == str2[n - 1]:
        return 1 + recursive_lcs(str1, str2, m - 1, n - 1)
    
    return max(recursive_lcs(str1, str2, m - 1, n), recursive_lcs(str1, str2, m, n - 1))

def non_recursive_lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    lcs = []
    for i in range(m + 1):
        lcs.append([None] * (n + 1))
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[m][n]

print recursive_lcs("AGGTAB", "GXTXAYB", 6, 7)
print non_recursive_lcs("AGGTAB", "GXTXAYB")