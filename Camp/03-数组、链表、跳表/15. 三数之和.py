# -*- coding: utf-8 -*-
# @Time     : 2020/8/16-16:49
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 15. 三数之和.py
# @Project  : Happy-Algorithm
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        res = []
        i = 0
        j = len(nums) - 1
        while (i < j):
            for k in range(i + 1, j):
                if nums[i] + nums[k] + nums[j] == 0:
                    res.append([nums[i], nums[k], nums[j]])
                elif nums[i] + nums[k] + nums[j] < 0:
                    i += 1
                else:
                    j -= 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    res = solution.threeSum(nums=nums)
    print(res)
