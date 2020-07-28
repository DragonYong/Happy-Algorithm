class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True, s[0] in wordDict]
        print(dp)
        for i in range(1, len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict and dp[j]:
                    dp.append(True)
                    break
            else:
                dp.append(False)

        return dp[-1]


s = "leetcode"
wordDict = ["le", "et", "code"]
print(Solution().wordBreak(s, wordDict))
