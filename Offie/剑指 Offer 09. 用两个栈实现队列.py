class CQueue1:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        while self.stack1:
            self.stack2.insert(0, self.stack1.pop(0))
        self.stack2.insert(value, 0)
        while self.stack2:
            self.stack1.insert(0, self.stack2.pop(0))

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop(0)


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        # 1 -> 2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # add value
        self.stack1.append(value)
        # 1 <- 2
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop()


# CQueue().appendTail(1)
# print()

a = [2, 3, 6, 89, 6]
print(a.pop(0))
# 这个题很奇怪,下面的方法通过列表的尾部可以算处理啊,通过头部算不出来
