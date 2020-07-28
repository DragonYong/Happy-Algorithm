class Solution:
    def exist(self, board, word: str) -> bool:
        # res = False
        # dp = [[False for i in range(len(item))] for item in board]
        # print(dp)
        # return res
        # 使用深度优先搜索
        if not board:  # 边界条件
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:  # 如果单词已经检查完毕
            return True

        # 如果路径出界或者矩阵中的值不是word的首字母,返回False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        tmp = board[i][j]  # 如果找到了第一额字母,检查剩余部分
        board[i][j] = '0'
        res = self.dfs(board, i+1, j, word[1:]) or \
            self.dfs(board, i-1, j, word[1:]) or \
            self.dfs(board, i, j+1, word[1:]) or \
            self.dfs(board, i, j-1, word[1:])   # 上下左右四个方向搜索

        board[i][j] = tmp
        return res


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(Solution().exist(board, word))


# 这道题, 好像没有找到前后之间的关系
# 1. 初始点怎么找
# 2. 结尾点怎么找
# 3. 已经使用过的怎么解决
# ---------------
# 最后发现不是用动态规划解决的,需要用到回溯
