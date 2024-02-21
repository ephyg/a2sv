class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]<nums[i]:
                numbers=ceil(nums[i]/nums[i+1])
                nums[i]=nums[i]//numbers
                ans+=(numbers-1)
        return ans

