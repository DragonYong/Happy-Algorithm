# -*- coding: utf-8 -*-
# @Time     : 2020/8/19-09:51
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 771. 宝石与石头.py
# @Project  : Happy-Algorithm
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        # for i in J:
        #     for j in S:
        #         if i == j:
        #             res += 1
        stone = {}
        for i in S:
            if stone.get(i):
                stone[i] += 1
            else:
                stone[i] = 1
        for i in J:
            if stone.get(i):
                res += stone[i]
        return res


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    solution = Solution()
    print(solution.numJewelsInStones(J, S))

    # 发现尽量多用内存，多循环拆分层单个巡航，效率会提高
