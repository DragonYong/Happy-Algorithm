# -*- coding: utf-8 -*-
# @Time     : 2020/8/19-10:45
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 8. 字符串转换整数 (atoi).py
# @Project  : Happy-Algorithm
class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0: return 0
        ls = list(str.strip())
        if len(ls) == 0: return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1

        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


if __name__ == '__main__':
    s = " "
    solution = Solution()
    print(solution.myAtoi(s))
