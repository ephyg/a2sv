class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot=0
        max_=nums[0]
        for i in range(len(nums)):
            tot+=nums[i]
            max_=max(max_,tot)
            if tot<0:
                tot=0     
        return max_
    