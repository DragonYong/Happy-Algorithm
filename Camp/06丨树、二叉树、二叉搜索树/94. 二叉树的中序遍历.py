#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/8/31-17:40
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 94. 二叉树的中序遍历.py
# @Project  : Happy-Algorithm
# *************************************************
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # if root is None:
        #     pass
        # if root.left != None:
        #     self.inorderTraversal(root.left)
        # res.append(root.val)
        # if root.right != None:
        #     self.inorderTraversal(root.right)
        # return res
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    instr = []
    solution = Solution()
    print(solution.inorderTraversal(instr))
