# -*- coding: utf-8 -*-
# @Time     : 2020/8/22-17:07
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 变态跳台阶.py
# @Project  : Happy-Algorithm
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # dp = [0] * (number + 1)
        # if number==1:
        #     dp[1] = 1
        # if number >= 2:
        #     dp[2] = 2
        # for i in range(3, number + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[number]
        if number <= 1:
            return 1
        else:
            return 2 ** (number - 1)


if __name__ == '__main__':
    solution = Solution()
    number = 7
    res = solution.jumpFloorII(number=number)
    print(res)
