class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero=0
        left=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            while zero>1:
                if nums[left]==0:
                    zero -=1
                left+=1
            ans=max(ans,i-left)
        return ans

