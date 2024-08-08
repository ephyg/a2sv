# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]*=2
                nums[i+1]=0
        l=0
        r=0
        while l<len(nums) and r<len(nums):
            if(nums[l]==0):
                if(nums[r]==0):
                    r+=1
                else:
                    nums[l],nums[r]=nums[r],nums[l]
            else:
                l+=1
                r+=1
        return nums
        