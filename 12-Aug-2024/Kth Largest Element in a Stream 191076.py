# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=nums
        self.k=k
        self.kthlargest=nlargest(k,self.heap)

    def add(self, val: int) -> int:
        if self.kthlargest and self.k<=len(self.kthlargest):
            if val>self.kthlargest[-1]:
                self.kthlargest.pop()
                self.kthlargest.append(val)
                self.kthlargest=nlargest(self.k,self.kthlargest)
        else:
            self.kthlargest.append(val)
            self.kthlargest=nlargest(self.k,self.kthlargest)


        return self.kthlargest[-1]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)