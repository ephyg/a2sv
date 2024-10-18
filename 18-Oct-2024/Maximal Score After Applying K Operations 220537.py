# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,-num)
        score = 0
        for i in range(k):
            score += (-heap[0])
            heappush(heap,-ceil(-heappop(heap)/3))
        return score
