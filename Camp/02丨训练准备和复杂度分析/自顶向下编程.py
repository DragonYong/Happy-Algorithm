# -*- coding: utf-8 -*-
# @Time     : 2020/8/15-18:13
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 自顶向下编程.py
# @Project  : Happy-Algorithm


class Solution(object):
    def merge(self, param, param1):

        res = []
        while (param1 and param):
            if param[0] <= param1[0]:
                res.append(param.pop(0))
            else:
                res.append(param1.pop(0))
        while param:
            res.append(param.pop(0))
        while param1:
            res.append(param1.pop(0))

        return res

    def merge_sort(self, data):
        if len(data) < 2:
            return data
        mid = len(data) // 2
        return self.merge(self.merge_sort(data[:mid]), self.merge_sort(data[mid:]))


if __name__ == '__main__':
    solution = Solution()
    import numpy as np

    data = np.random.randint(0, 100, 30)
    print("原始数据:", data)
    res = solution.merge_sort(list(data))
    print("排序完成：", res)
