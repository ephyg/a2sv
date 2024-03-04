class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def subset(curr,cand):
            if tuple(curr) in ans:
                return 
            if len(curr)<=len(nums):
                ans.add(tuple(sorted(curr[:])))
            for i in range(len(cand)):
                curr.append(cand[i])
                subset(curr,cand[i+1:])
                curr.pop()
        subset([],nums)
        return ans
