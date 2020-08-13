# -*- coding: utf-8 -*-
# @Time     : 2020/8/13-16:19
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 剑指 Offer 04. 二维数组中的查找.py
# @Project  : Happy-Algorithm

class Solution:
    def findNumberIn2DArray(self, matrix, target):
        n = len(matrix[0])
        m = len(matrix)
        # print(m, n)
        temp=0

        while n and m:
            if target < matrix[m][n]:
                n -= 1
            elif target > matrix[m][n]:
                m+= 1


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    target = 5
    solution = Solution()
    print(solution.findNumberIn2DArray(matrix, target))
