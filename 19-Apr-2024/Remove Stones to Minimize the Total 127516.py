# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        for num in piles:
            heappush(heap,-num)
        for i in range(k):
            x=ceil(-heappop(heap)/2)
            heappush(heap,-x)
        return -sum(heap)