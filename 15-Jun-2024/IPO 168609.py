# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        Heap=[(capital[i],-profits[i]) for i in range(len(capital))]
        heapify(Heap)
        capitalHeap=[]

        for i in range(k):
            while Heap and w>=Heap[0][0]:
                heappush(capitalHeap,heappop(Heap)[::-1])
            if capitalHeap:
                w+=(-heappop(capitalHeap)[0])
                
        return w