# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def detection(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False

            if l.val != r.val:
                return False

            return detection(l.left, r.right) and detection(l.right, r.left)

        return detection(root.left, root.right)


# 这道题, 难点在于需要返回的是True/False, 当时递归需要返回
# 的是根结点, 索引, 必须的在生命一个函数, 原本函数返回值, 来
# 自于自己定义的函数
#

# 还有需要注意的是对称, 左左右右, 左右右左对称才想, 四种情况

def isSymmetric(root):
    if root is None:
        return True
    left = self.isSymmetric(root.left)
    right = self.isSymmetric(root.right)
    return left.val and right.val


# 上面这行代码就是典型的错误, 终止是返回boolearn, 但是
# 最后又返回节点的值
# 单个值返回判断,不容易,就根据子节点,进行四个值比较
