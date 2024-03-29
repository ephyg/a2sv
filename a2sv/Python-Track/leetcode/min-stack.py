class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimum=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or self.minimum[-1]>=val:
            self.minimum.append(val)
    def pop(self) -> None:
        if self.stack[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()