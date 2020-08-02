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

# 现在看来,他是确保前面i的是存在字典,然后接着早已一个区间的(i,j)是否存在,如果存在,.则吧下界当成行的上界
# 和着我面试的时候, .遍历字符串, 然后左边切除差不多,不过他可以却确保,字典里的两个单词长短不一,导致短词先
# 占用,它这里面的第二个循环就是为了解决短的字符提前终止
