class Solution:
    def twoSum(self, numbers, target):
        res = [-1, -1]
        # length = len(numbers)
        # for i in range(length):
        #     for j in range(1, length):
        #         if numbers[i]+numbers[j] == target:
        #             res = [i+1, j+1]

        left = 0
        right = len(numbers)-1
        while left < right:
            total = numbers[left]+numbers[right]
            if target == total:
                print(left)
                res = [left+1, right+1]
            elif target > total:
                left += 1
            elif target < total:
                right -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(numbers, target))

# 两个for循环,复杂度有点大,可以考虑双指针
