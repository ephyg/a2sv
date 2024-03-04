class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        def combine(curr,_sum):
            if _sum==target:
                ans.add(tuple(sorted(curr[:])))
            if _sum>target:
                return 
            visited=set()
            for i in range(len(candidates)):
                if candidates[i] in visited:
                    continue
                _sum+=candidates[i]
                curr.append(candidates[i])
                combine(curr,_sum)
                visited.add(candidates[i])
                _sum-=candidates[i]
                curr.pop()
        combine([],0)
        return ans