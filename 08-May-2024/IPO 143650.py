# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        Heap=[]
        capitalHeap=[]
        for i,num in enumerate(profits):
            heappush(Heap,(capital[i],-num))
        for i in range(k):
            while Heap and w>=Heap[0][0]:
                x,y=heappop(Heap)
                heappush(capitalHeap,(y,x))
            if capitalHeap:
                w+=(-heappop(capitalHeap)[0])
        
        return w