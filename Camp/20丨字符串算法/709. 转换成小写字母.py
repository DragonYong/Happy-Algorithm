# -*- coding: utf-8 -*-
# @Time     : 2020/8/19-09:23
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 709. 转换成小写字母.py
# @Project  : Happy-Algorithm
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for i in str:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                res += i
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                res += (chr(ord(i) + 32))
            else:
                res += i
        return res


if __name__ == '__main__':
    chrs = "Apple"
    solution = Solution()
    print(solution.toLowerCase(chrs))
    print(chr(97))
