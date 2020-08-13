# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # if root.left is None:
        #     left = 0
        #     return False
        # if root.right is None:
        #     right = 0
        #     return False
        # if self.isBalanced(root.left):
        #     left += 1
        # if self.isBalanced(root.right):
        #     right += 1
        # return abs(left-right) < 2
        if not root:
            return True
        return abs(self.depth(root.left)-self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1
