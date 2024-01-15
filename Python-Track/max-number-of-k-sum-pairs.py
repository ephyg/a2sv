class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-1
        op=0
        nums.sort()
        while r>l:
            tot=nums[l]+nums[r]
            if tot==k:
                op+=1
                l+=1
                r-=1
            elif tot>k:
                r-=1
            else:
                l+=1
        return op