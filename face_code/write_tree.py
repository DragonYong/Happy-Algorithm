# -*- coding: utf-8 -*-
# @Time     : 2020/8/29-14:58
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : write_tree.py
# @Project  : Happy-Algorithm

class TreeNode(object):
    def __init__(self):
        self.data = 1
        self.left = None
        self.right = None

    def preorder(self, root):
        if root is None:
            return
        else:
            print(root.data)
            self.innorder(root.left)
            self.innorder(root.right)

    def innorder(self, root):
        if root is None:
            return
        else:
            self.innorder(root.left)
            print(root.data)
            self.innorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def get(self, param):
        self.data = [1, 2, 3]

    def add(self, param):
        self.data = param
        self.left = None
        self.right = None


if __name__ == '__main__':
    tree = TreeNode()
    tree.add(1)
    tree.add(2)
    root = tree.get(1)
    tree.preorder(root)
    tree.innorder(root)
    tree.postorder(root)
