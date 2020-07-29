class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
                print(dp[i])

        return dp[-1] % 1000000007


print(Solution().cuttingRope(2))

# 这道题和第一题的区别,数字更大,使得它可能越界
# 注意:这里有取余,当时又有大小比较,所以的谨慎了

# 投机取巧的方法就是,中间计算的时候,不进行取余,而是返回的是后进行取余
