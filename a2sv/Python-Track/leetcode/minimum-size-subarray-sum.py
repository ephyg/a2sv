class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _min=float("inf")
        l=0
        r=0
        tot=0
        while r<len(nums):
            while target>tot and r<len(nums):
                tot+=nums[r]
                r+=1
            while target<=tot:
                _min=min(_min,r-l)
                tot-=nums[l]
                l+=1

        if _min==float("inf"):
            return 0
        return _min