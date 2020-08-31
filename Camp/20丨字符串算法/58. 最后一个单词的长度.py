# -*- coding: utf-8 -*-
# @Time     : 2020/8/19-09:38
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 58. 最后一个单词的长度.py
# @Project  : Happy-Algorithm
# https://leetcode-cn.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = ''
        if s is "": return 0
        # if s[-1] is " ":
        #     s = s[:-1]
        s = s.strip()

        for i in s:
            if i is " ":
                temp = ''
            else:
                temp += i
        # print(temp)
        res = len(temp)
        return res


if __name__ == '__main__':
    s = "Hello World "
    solution = Solution()
    print(solution.lengthOfLastWord(s))
