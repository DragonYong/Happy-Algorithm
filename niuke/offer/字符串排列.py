# -*- coding: utf-8 -*-
# @Time     : 2020/8/22-07:39
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 字符串排列.py
# @Project  : Happy-Algorithm
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        str = list(ss)
        self.permutation_trans(str, 0)
        return ss

    def permutation_trans(self, str, start):
        if str == None or start < 0:
            return
        if start == len(str) - 1:
            print(''.join(str), end=' ')
        else:
            i = start
            while i < len(str):
                str[start], str[i] = str[i], str[start]
                self.permutation_trans(str, start + 1)
                str[start], str[i] = str[i], str[start]
                i += 1


if __name__ == '__main__':
    ss = "acb"
    solution = Solution()
    res = solution.Permutation(ss=ss)
    print(res)
# ≠≠≠≠––––≠≠