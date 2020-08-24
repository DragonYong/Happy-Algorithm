# -*- coding: utf-8 -*-
# @Time     : 2020/8/19-10:04
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 387. 字符串中的第一个唯一字符.py
# @Project  : Happy-Algorithm
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # store = {}
        # for i in s:
        #     if store.get(i):
        #         store[i] += 1
        #     else:
        #         store[i] = 1
        #
        # for i in range(len(s)):
        #     if store[s[i]] == 1:
        #         return i

        store = Counter(s)
        # print(store)
        for i, item in enumerate(s):
            if store[item] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = 'loveleetcode'
    solution = Solution()
    print(solution.firstUniqChar(s))

    # 参照官网的，使用enumerate果然效率高了好多
