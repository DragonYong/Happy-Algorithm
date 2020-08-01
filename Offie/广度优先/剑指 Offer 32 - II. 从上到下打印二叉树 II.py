# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
       if not root:
           return []

        res,queue=[],collections.deque()
        queue.append(root)
        while queue:
            tmp=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                tmp.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            res.append(tmp)
        return res

# 这道题,知道是广度遍历,需要使用队列,当时无从下手,的仔细研究琢磨
