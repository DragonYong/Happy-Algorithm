# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left, root.right = root.right, root.left
        return root


# 这道题难在,终止条件如何设置

# 返回的时候,是当前根结点获取子节点,然后吧根结点的孩子换了
