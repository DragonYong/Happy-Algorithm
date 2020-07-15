class CQueue:

    def __init__(self):
        self.stack1 = [2,3]
        self.stack2 = []
        self.size = 0

    def appendTail(self, value):
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())

    def deleteHead(self):
        if len(self.stack1)==0:
            return -1
        res = self.stack1.pop()
        return res

# Your CQueue object will be instantiated and called as such:
value = 1
obj = CQueue()
obj.appendTail(value)
param_2 = obj.deleteHead()
