class Solution:

    # 递归算法超时
    def max3(self, i, j, k):
        return max(i, max(j, k))

    # def cuttingRope(self, n: int) -> int:
    #     memo = [-1]*(n+1)
    #     if n == 1:
    #         return 1
    #     if memo[n] != -1:
    #         return memo[n]
    #     res = -1
    #     for i in range(1, n):
    #         # i + (n-i)
    #         res = self.max3(res,  i*self.cuttingRope(n-i),
    #                         i*(n-i))  # 最后一个是确保只分割成两部分
    #     memo[n] = res

    #     return res
    def cuttingRope(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = self.max3(dp[i], j*(i-j), j*dp[i-j])

        return dp[-1]


print(Solution().cuttingRope(10))

# 这个递推关系搞不清
# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1）
# ，每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1]
# 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、
# 3的三段，此时得到的最大乘积是18。


# 这道题和343. integer break有同解

# 使用动态规明显很容易解出这道题的答案
