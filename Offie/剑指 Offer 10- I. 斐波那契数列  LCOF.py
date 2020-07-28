class Solution:
    # def __init__(self):
    #     self.memo = [0]

    # def fib(self, n: int) -> int:

    #     self.memo = self.memo*(n+1)

    #     if n < 0:
    #         return -1
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1

    #     if self.memo[n] == 0:
    #         self.memo[n] = self.fib(n-1)+self.fib(n-2)
    #     return self.memo[n]
    def fib(self, n: int) -> int:
        res = [0]*(n+1)
        res[0] = 0
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i-2]+res[i-1]
        return res[0]


print(Solution().fib(1))


# 这道题很奇怪,记忆化搜索,递归深层的还是出错
