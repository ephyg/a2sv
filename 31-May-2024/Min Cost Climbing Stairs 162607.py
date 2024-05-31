# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        cost=cost[::-1]
        for i in range(2,len(cost)):
            cost[i]=min(cost[i-2],cost[i-1])+cost[i]
        return min(cost[-1],cost[-2])
        