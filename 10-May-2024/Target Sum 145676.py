# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dp(idx,total):
            if total==target and idx==len(nums):
                return 1

            if idx>=len(nums):
                return 0
            if (idx,total) not in memo:
                memo[(idx,total)]=dp(idx+1,total-nums[idx])+dp(idx+1,total+nums[idx])
            return memo[(idx,total)]
        return dp(0,0)

