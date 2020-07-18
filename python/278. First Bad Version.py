# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # version 1 for loop
        # for i in range(1, n+1):
        #     if isBadVersion(i):
        #         pass
        #     else:
        #         return i
        rul = n
        left = 1
        right = n

        while left <= right:
            midd = (right-left)//2+left
            if isBadVersion(midd):
                right = midd-1
                rul = midd
            else:
                left = midd+1
        return rul


if __name__ == "__main__":
    solution = Solution()
    n = 123
    print(solution.firstBadVersion(n))

# but this method is wrong, it cost more time to solve this problem

# so i want to use midd-find for this problem


# midd find templete
# left = 0
# right = length-1
# rul = n
# while left <= right:
#     if target <= midd:
#         right = mid-1
#         rul = mid
#     else:
#         left += mid
# return rul
