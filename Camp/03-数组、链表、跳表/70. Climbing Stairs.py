# -*- coding: utf-8 -*-
# @Time     : 2020/8/16-16:33
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 70. Climbing Stairs.py
# @Project  : Happy-Algorithm

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        if n>1:
            dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    res = solution.climbStairs(7)
    print(res)
