# -*- coding: utf-8 -*-
# @Time     : 2020/8/25-10:03
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : sort012.py
# @Project  : Happy-Algorithm
# 75. 颜色分类
# https://leetcode-cn.com/problems/sort-colors/


def sort_0_1_2(nums):
    """
    阳光出行，有点鄙视非科班人
    :param nums:
    :return:
    """
    left = 0
    right = len(nums) - 1

    i = 0
    while i <= right:
        if nums[i] == 0:
            left += 1
            if i != left:
                nums[i], nums[left] = nums[left], nums[i]

        elif nums[i] == 2:
            right -= 1
            if i != right:
                nums[i], nums[right] = nums[right], nums[i]

        i += 1
    print(nums)


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 1, 2, 0, 0, 1, 2, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0]
    sort_0_1_2(nums)
