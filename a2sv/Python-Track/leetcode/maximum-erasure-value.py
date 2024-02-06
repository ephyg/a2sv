class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        _max=0
        dict=defaultdict(int)
        l=0
        r=0
        ans=0
        while r<len(nums):
            dict[nums[r]]+=1
            while dict[nums[r]]==2:
                dict[nums[l]]-=1
                if dict[nums[l]]==0:
                    dict.pop(nums[l])
                l+=1
            _sum=sum(nums[l:r+1])
            if _sum>ans:
                ans=_sum
            r+=1
        return ans
