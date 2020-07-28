class Solution:
    def maxSlidingWindow(self, nums, k):
        if len(nums) < k:
            return []
        res = []
        right = len(nums)-k+1
        # print(right, "right")
        for i in range(right):
            # print(i)
            single = max(nums[i:i+k])
            # print(a[i:k], single)
            res.append(single)
        return res


a = [2, 4, 5, 7, 9, 7, 4, 6, 8, 2, 5, 8]
print(Solution().maxSlidingWindow(a, 3))


# 这个是在星药科技的面试题,很简单,怎么就做不出了???蠢!!!!!!!!!!
