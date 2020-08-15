# -*- coding: utf-8 -*-
# @Time     : 2020/8/13-21:14
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 91. 解码方法.py
# @Project  : Happy-Algorithm
class Solution:
    def numDecodings(self, s: str):
        # 这个是动态规划
        n = len(s)
        dp = [i for i in range(n+ 1)]
        print(dp)
        # for i in range(1, n + 1):
        #     if int(str[i - 1:i + 1]) <= 26:
        #         k = 1
        #     else:
        #         k = 0
        #     dp[i] = dp[i - 1] + 1 + k
        return dp [n]


s = "1223"

print(Solution().numDecodings(s))
