class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if s == " " or s == '' or len(s) == 1:
        #     return True
        # print(list(s))

        # print(queue)
        # if len(queue) < 2:
        #     return False
        # while (len(queue) > 1):
        #     if queue.pop(0) != queue.pop():
        #         return False

        queue = [i.lower() for i in list(s) if i.isalpha()]
        # return queue == queue[::-1]
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        print(sgood, type(sgood))
        print(queue, type(queue))
        print(queue == queue[::-1])
        print(sgood == sgood[::-1])
        return sgood == sgood[::-1]


if __name__ == "__main__":
    solution = Solution()
    s = "0P"
    print(solution.isPalindrome(s))


# 注意是字母还是数字和字母类型的两个函数
