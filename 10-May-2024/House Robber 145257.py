# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dp(idx):
            if idx<0:
                return 0
            if idx not in memo:
                memo[idx]=max(dp(idx-2)+nums[idx],dp(idx-1))
            return memo[idx]
        return dp(len(nums)-1)