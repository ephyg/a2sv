# Problem: Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        n=len(nums)
        for i in range(len(nums)//2):
            ans=max(nums[i]+nums[n-i-1],ans)
        return ans