def min_conversions(str1, str2):
    """
    Return the minimum number of operations can be performed
    on the str1 that it gets converted to str2. The operations can be:

    - Insert
    - Remove
    - Replace
    """
    m = len(str1)
    n = len(str2)

    dp = []
    for i in range(m + 1):
        dp.append([None] * (n + 1))

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + \
                    min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]))

    return dp[m][n]


print min_conversions("march", "cart")
