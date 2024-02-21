class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort( key = lambda x : x[0]-x[1])
        idx=len(costs)//2
        left=sum((list(zip(*costs)))[0][:idx])
        right=sum((list(zip(*costs)))[1][idx:])
        return right+left