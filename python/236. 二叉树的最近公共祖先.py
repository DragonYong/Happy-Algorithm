# 这道题和785是一样的, 都需要先判断没有根结点, 以及有一个值就是根结点的情况
# 然后分别遍历左右, 左边的如果为空, 返回右边, 右边为空, 返回左边,都不为空,这返回root
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        return root
