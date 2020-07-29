class Solution:
    def minNumber(self, nums) -> str:
        max_len = max([i for i in nums])
        m = max_len//10+1
        res = []
        for i in range(m):
            res.append([item for item in nums if (item//10) == i])
        # print(res)

        res1 = ''
        for item in res[::-1]:
            item.sort()
            print(item)
            if item:
                for i in item:
                    res1 += str(i)
                    print(res)

        return res1


nums = [3, 30, 34, 5, 9]
print(Solution().minNumber(nums))
