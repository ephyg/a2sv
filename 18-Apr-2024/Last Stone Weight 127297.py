# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        heap=[]
        for num in stones:
            heappush(heap,-num)
        while len(heap)>1:
            x=heappop(heap)
            y=heappop(heap)
            if x!=y:
                heappush(heap,-(-x-(-y)))
        return 0 if len(heap)==0 else -heap[0]
