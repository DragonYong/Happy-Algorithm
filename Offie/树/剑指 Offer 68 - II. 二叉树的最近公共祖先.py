class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # while root:
        #     if self.lowestCommonAncestor(root.left, p, q):
        #         root = root.left
        #     elif self.lowestCommonAncestor(root.right, p, q):
        #         root = root.right
        #     else:
        #         return root
        # return None
        ans = None

        def tree(current):
            if not current:
                return False
            left = tree(current.left)
            right = tree(current.right)
            mid = current == p or current == q

            if mid+left+right >= 2:
                self.ans = current
            return mid or left or right  # 查找这三个点是否存在
        tree(root)
        return self.ans


# 这道题和原题的不同在于不是搜索树,所以判断的条件会不同
