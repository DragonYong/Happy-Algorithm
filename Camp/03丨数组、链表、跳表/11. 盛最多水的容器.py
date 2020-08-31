# -*- coding: utf-8 -*-
# @Time     : 2020/8/16-15:23
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 11. 盛最多水的容器.py
# @Project  : Happy-Algorithm
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双循环会浪费很多时间
        :param height:
        :return:
        """
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         if (j - i) * min(height[j], height[i]) > res:
        #             res = (j - i) * min(height[j], height[i])
        # print(res)
        res = 0
        i = 0
        j = len(height) - 1
        while (i < j):
            """每次先动个子矮的"""
            # if (j - i) * min(height[i], height[j]) > res:
            #     res = (j - i) * min(height[i], height[j])
            # if height[i] < height[j]:
            #     i += 1
            # else:
            #     j -= 1
            if height[i] < height[j]:
                temp = (j - i) * height[i]
                i += 1
            else:
                temp = (j - i) * height[j]
                j -= 1
            res = max(res, temp)
        return res


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    res = solution.maxArea(height=height)
    print(res)
