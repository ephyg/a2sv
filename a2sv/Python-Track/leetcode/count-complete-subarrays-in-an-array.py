class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dist=len(set(nums))
        count=0
        for i in range(len(nums)):
            x=set()
            for j in range(i,len(nums)):
                x.add(nums[j])
                if len(x)==dist:
                    count+=1
        return count