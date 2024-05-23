# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        nums=[(efficiency[i],speed[i]) for i in range(n)]
        nums.sort(reverse=True)
        mod=10**9 + 7
        heap=[]
        total=0
        max_=0
        for i in range(n):
            if len(heap)==k:
                total-=heappop(heap)
            heappush(heap,nums[i][1])
            total+=nums[i][1]
            max_=max(max_,nums[i][0]*total)
        return max_%mod
            