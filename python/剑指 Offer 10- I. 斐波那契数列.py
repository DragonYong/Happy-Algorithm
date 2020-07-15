class Solution:
    def fib(self, n: int) -> int:
        memo = [-1 for i in range(n+2)]
        # print(memo)
        
        memo[0] = 0
        
        memo[1] = 1
        # print(memo)

        for i in range(2,n+1):
        	memo[i] = memo[i-1] + memo[i-2]

        return memo[n]


s = Solution()
print(s.fib(5))
