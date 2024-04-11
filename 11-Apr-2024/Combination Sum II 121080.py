# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def combine(idx, arr, _sum):
            if _sum == target:
                ans.add(tuple(sorted(arr[:])))
                return

            if _sum > target:
                return
                
            visited = set()
            for i in range(idx, len(candidates)):
                if not candidates[i] in visited:
                    arr.append(candidates[i])
                    _sum += candidates[i]
                    combine(i + 1, arr, _sum)
                    visited.add(candidates[i])
                    _sum -= candidates[i]
                    arr.pop()
        combine(0, [], 0)
        return ans
