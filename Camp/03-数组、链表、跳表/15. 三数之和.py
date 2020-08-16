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
        n = len(nums)
        nums.sort()  # 先排序
        ans = []
        for first in range(n - 2):  # 枚举第一个元素
            if nums[first] > 0: break  # 数组里最小的都大于0 不可能有答案
            if first > 0 and nums[first] == nums[first - 1]: continue  # 保证first不会有重复
            # 以下作为标准双指针写法
            second, third = first + 1, n - 1
            while second < third:
                target = 0 - nums[first]
                s = nums[second] + nums[third]
                if s > target:  # 当前数值太大 做出决策：右指针左移
                    third -= 1  # 左移后有重复没关系 重复的就肯定又回来这里减1啦
                elif s < target:  # 当前数值太小 做出决策：左指针右移
                    second += 1
                else:  # 前数值正合适 做出决策：左指针右移且右指针左移 注意不能重复
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while third > second and nums[third] == nums[third + 1]: third -= 1
                    while third > second and nums[second] == nums[second - 1]: second += 1
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    res = solution.threeSum(nums=nums)
    print(res)
