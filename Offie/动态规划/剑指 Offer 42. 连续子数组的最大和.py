class Solution:
    def maxSubArray(self, nums) -> int:

        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            # 当dp[i-1]产生负相关,这重新取值
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            # print(dp[i])
        # print(dp)
        return max(dp)


nums = [-2, 1]
print(Solution().maxSubArray(nums))

# 字符串求值,大部分都可以使用动态规划
# 1. 确定前后关系
# 2. 找临界点


# 这道题答案很奇怪,最后的返回是这个数组的最大值
