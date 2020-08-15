# -*- coding: utf-8 -*-
# @Time     : 2020/8/13-16:19
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 剑指 Offer 04. 二维数组中的查找.py
# @Project  : Happy-Algorithm

class Solution:
    def findNumberIn2DArray(self, matrix, target):
        n = len(matrix[0]) - 1
        m = len(matrix) - 1
        i = m
        j = 0
        while i >= 0 and j <= n:
            if target > matrix[i][j]:
                j += 1
            elif target < matrix[i][j]:
                i -= 1
            else:
                return True
        return True

        # # print(m, n)　
        # temp = 0
        # i = m
        # while n and i <= m:
        #     if target < matrix[m - i][n]:
        #         n -= 1
        #     elif target > matrix[m - i][n]:
        #         i += 1
        #     elif target == matrix[m - i][n]:
        #         return True
        # return False


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
