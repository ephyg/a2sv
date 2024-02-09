class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        product = 1
        subarrays = 0
        if k<=1:
            return 0
        while r < len(nums):
            product*= nums[r]
            while product>=k:
                product//=nums[l]
                l+=1
            subarrays+=(r-l+1)
            r+=1
        return subarrays