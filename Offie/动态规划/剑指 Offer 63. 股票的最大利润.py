class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        dp = [0]*len(prices)
        get = [0]*len(prices)
        for i in range(1, len(prices)):
            get[i] = prices[i]-prices[i-1]
        get[0] = -7
        # print(prices)
        dp[0] = 0
        for i in range(1, len(get)):
            dp[i] = max(dp[i-1]+get[i], get[i])
        return max(dp)


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))


# 这里要注意:临界条件小于2的时候,是没有收益的
转移方程的时候, 通过收益进行转移方便, 如果直接写销售价格, 可能会不方便
#
