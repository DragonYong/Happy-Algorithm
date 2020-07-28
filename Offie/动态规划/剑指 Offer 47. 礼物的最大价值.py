class Solution:
    def maxValue(self, grid) -> int:

        dp = [[0]*len(item) for item in grid]
        dp[0][0] = grid[0][0]
        # print(dp)
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        # print(grid)
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        # print(dp)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])+grid[i][j]
        # print(dp)
        # dp[0][0] = grid[0][0]
        return dp[-1][-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(Solution().maxValue(grid))


# 这道题的难点是第一个值, 初始化为0, 需要改成矩阵的第一个值
