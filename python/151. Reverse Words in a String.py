class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or s = "":
            return None

        s = s.strip()

        temp = s.split(" ")
        for i in temp:
            print("${}$".format(i))
        stack = [i for i in temp if i != ""]
        return " ".join(stack[::-1])


if __name__ == "__main__":
    solution = Solution()
    s = "the sky is blue"
    s = "a good       example"
    print(solution.reverseWords(s))

# 这道通主要是注意细节,中间空格可能会有跟多个,需要吧多余的空格全部删除,还有就是临界的情况,队医空的输入没,需要异常捕获
