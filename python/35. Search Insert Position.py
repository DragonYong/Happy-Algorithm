class Solution:
    def searchInsert(self, nums, target: int) -> int:
        mid = (len(nums)-1)//2
        left = 0
        res = len(nums)
        right = res-1
        while left <= right:
            mid = (right-left) // 2 + left
            if target <= nums[mid]:
                right = mid-1
                res = mid
            else:
                left = mid+1

        # for i in range(len(nums)):
        #     if target > nums[i]:
        #         pass
        #     else:
        #         return i
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 90
    print(solution.searchInsert(nums, target))
    # tage = None
    # print(1 if not tage else 0)

# 这道题需要注意最后一个位置的情况,在判断语句里面是没有的,需要在最后面自己添加
# 可以尝试折半的方法,这样回省一半的时间
# 折半查找时间发诈度是O(log n)
