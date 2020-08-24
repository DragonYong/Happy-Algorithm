# -*- coding: utf-8 -*-
# @Time     : 2020/8/22-17:17
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 取近似值.py
# @Project  : Happy-Algorithm



class Solution(object):
    def get_sim_value(self, number):
        res = int(number + 0.51)
        return res



if __name__ == '__main__':
    number =0.8
    solution = Solution()
    res = solution.get_sim_value(number)
    print(res)
