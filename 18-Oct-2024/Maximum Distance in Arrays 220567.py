# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_heap = []
        min_heap = []

        for i in range(len(arrays)):
            heappush(min_heap,(arrays[i][0],i))
            heappush(max_heap,(-arrays[i][-1],i))

        if max_heap[0][1] == min_heap[0][1]:
            x = -heappop(max_heap)[0]
            y = heappop(min_heap)[0]
            
            return max(-max_heap[0][0]-y,x-min_heap[0][0])
        return -max_heap[0][0]-min_heap[0][0]



            