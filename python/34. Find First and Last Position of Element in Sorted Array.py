class Solution:

    def binary_find_last(self, nums, target):
        """
        this is find the last data
        """
        low = 0
        hight = len(nums)-1
        first = True
        while low <= hight:
            mid = (hight-low)//2+low
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hight = mid-1
            else:
                low = mid+1
        return -1

    def searchRange(self, nums, target: int):
        rul = self.binary_find_last(nums, target)

        # left = 0
        # right = len(nums)-1
        # rul = [-1]*2
        # while left <= right:
        #     mid = (right-left)//2+left

        #     if nums[mid] == target:
        #         rul[0] = mid
        #     elif nums[mid] > target:
        #         right = mid-1

        #     else:
        #         left = mid+1

        # print(rul)
        # rul = [-1]*2
        # # find first data index
        # left = 0
        # right = len(nums)-1
        # index = 0
        # while left <= right:
        #     mid = (right-left)//2+left
        #     if target <= nums[mid]:
        #         right = mid-1
        #         index = mid
        #     else:
        #         left = mid+1
        # # print(index)
        # rul[0] = index
        # if index == -1:
        #     return rul
        # left = 0
        # right = len(nums)-1
        # index = 0
        # target += 1
        # while left <= right:
        #     mid = (right-left)//2+left
        #     if target <= nums[mid]:
        #         right = mid-1
        #         index = mid
        #     else:
        #         left = mid+1
        # rul[1] = index
        return rul

# def test_mid_find(nums, target):
#     left = 0
#     right = len(nums)-1
#     index = -1
#     while left <= right:
#         mid = (right-left)//2+left
#         if target <= nums[mid]:
#             right = mid-1
#             index = mid
#         else:
#             left = mid+1
#     return index

# up method is wrong, for the fiorst data and unknow data for result 0


def binary_find(nums, target):
    low = 0
    hight = len(nums)-1
    while low <= hight:
        mid = (hight-low)//2+low
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hight = mid-1
        else:
            low = mid+1
    return -1


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 7
    sol = Solution()
    print(sol.searchRange(nums, target))
    # print(test_mid_find(nums, target))
    # print(binary_find(nums, target))

# it need complexity must be in the order of O(logn)
# so use midd find
