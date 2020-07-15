"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int) -> int:
        memo = [1]*(n+1)

        for i in range(2, n+1):
            sum = 0
            for j in range(1, i+1):
                sum += memo[j-1]*memo[i-j]
            memo[i] = sum
        return memo[n]

    def numTrees1(self, n: int) -> int:
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.numTrees(4))
"""
当n=1:1
当n=2:2[null,arr]
当n=3:5[[null,arr],[arr,arr],[null,arr]]
可以看出当n=3的时候会用到n=2的数据,所以可以使用记忆化搜索
"""
