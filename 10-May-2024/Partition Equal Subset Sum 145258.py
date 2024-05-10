# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo={}
        def dp(idx,target):
            if target==0:
                return True

            if idx>len(nums)-1 or target<0:
                return False

            if (idx,target) not in memo:
                memo[(idx,target)]=dp(idx+1,target-nums[idx]) or dp(idx+1,target)
            return memo[(idx,target)]

        
        tot=sum(nums)
        if tot%2:
            return False

        return dp(0,tot//2)