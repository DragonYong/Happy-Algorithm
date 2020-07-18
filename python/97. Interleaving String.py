# https://leetcode-cn.com/problems/interleaving-string/
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        rul = False

        # while s3:
        #     tag = s3[0]
        #     s3 = s3[1:]
        #     if s1:
        #         a = s1[0]
        #     else:
        #         a = None
        #     if s2:
        #         b = s2[0]
        #     else:
        #         b = None
        #     if tag == a:
        #         s1 = s1[1:]
        #     elif tag == b:
        #         s2 = s2[1:]
        #     else:
        #         return rul
        # rul = True
        return rul


if __name__ == "__main__":
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # print(s3[0])
    print(sol.isInterleave(s1, s2, s3))
    print(s1+s2)

# by three thread is wrong!!!!
