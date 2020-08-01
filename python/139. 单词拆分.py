class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        # print(dp)
        # 定义初始条件
        dp[0] = True

        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in wordDict):
                    # 归纳条件
                    dp[j] = True
        return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))

# 这是星药科技面试题,当时怎么也没想到动态规划俩解决,因为都是
# 字符串,没法想到怎么两者之间如何产生关联,用了朴素的方法,字符串
# 切片,遍历词典,当时这样面面试不成

# 现在看来,遍历字符串,贪心的寻找最大子串,开始索引又归0,确保最后一部分字符串还在字典里,就能确保了
