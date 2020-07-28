class Solution:

    def fib(self, n: int) -> int:
        dp = [1]*(n+1)
        dp[0] = 0
        # dp[1]=1
        for i in range(2, n+1):
            # print(dp)
            # print(dp[i-1]+dp[i-2])
            dp[i] = (dp[i-1]+dp[i-2]) % 1000000007

        return dp


print(Solution().fib(0))


# 注意: 初始化的时候, 弄成全为1, 就会避免当n = 1的时候,
# 初始化第二个值的时候的错误
# 动态规划易动摇注意初始化两个条件之间的影响
