# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        heap=[]
        for i in range(len(profit)):
            heappush(heap,(-profit[i],difficulty[i]) )
        ans=0
        worker.sort(reverse=True)
        for num in worker:
            while heap and num < heap[0][1]:
                heappop(heap)
            if heap:
                ans+=(-heap[0][0])
        return ans
