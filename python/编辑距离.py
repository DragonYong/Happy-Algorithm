def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        dp[i][0] = i
    for i in range(m):
        dp[0][i] = i
    for i in range(1, n):
        for j in range(1, m):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+d)
    return dp[-1][-1]


s1 = 'apple'
s2 = 'aple'
print(edit_distance(s1, s2))
