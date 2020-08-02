# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root is None:
        #     return None
        # if root.val == p.val or root.val == q.val:
        #     return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

        # while root:
        #     if root.val > p.val and root.val > q.val:
        #         root = root.left
        #     elif root.val < p.val and root.val < q.val:
        #         root = root.right
        #     else:
        #         return root
        # return None


# 这个题很特殊,虽然是树的问题,但是不需要进行递归,从上往下一次就可以了
# 条件是确保该值在直接点中间即可
# 时间复杂度O(n)

# ----------
# 递归做这道题最好了,时间复杂度底,弄错了返回的情况,我写的时候,知识递归,忘了递归后需要返回
