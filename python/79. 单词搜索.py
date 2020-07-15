class Solution:
    def exist(self, board, word):
        d = {(-1, 0),
             (0, 1),
             (1, 0),
             (0, -1)}
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for i in range(m)]
        print(visited[1][0])
        def searchWord(board, word,index,startx,starty):
            visited[startx][starty]==word[index]


solution = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
res = solution.exist(board, 'w')
# print(res)


# a = [(-1, 0), (0, 1)]
# print(a)
