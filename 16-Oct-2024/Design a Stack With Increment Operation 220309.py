# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if self.maxSize > 0:
            self.stack.append(x)
            self.maxSize -= 1
        

    def pop(self) -> int:
        if self.stack:
            self.maxSize += 1
            return self.stack.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        i = 0
        while len(self.stack) > i and k > 0:
            self.stack[i] += val
            i += 1
            k -= 1
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)