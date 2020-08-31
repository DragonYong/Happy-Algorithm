# -*- coding: utf-8 -*-
# @Time     : 2020/8/16-15:56
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 283. 移动零.py
# @Project  : Happy-Algorithm
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        # for item in nums:
        #     if item != 0:
        #         nums[index] = item
        #         index += 1
        # for i in range(index, len(nums)):
        #     nums[i] = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[index], nums[j] = nums[j], nums[index]
                index += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    res = solution.moveZeroes(nums=nums)
    print(res)

    # 根据结果发现，for循环使用的越少越好
