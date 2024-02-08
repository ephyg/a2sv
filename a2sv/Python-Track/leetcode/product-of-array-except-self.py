class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=prod(nums[1:])
        ans=[prefix]
        for i in range(1,len(nums)):
            if nums[i]==0:
                prefix=prod(nums[i+1:])*(prod(nums[:i]))
                ans.append(prefix)
            else:
                prefix=(prefix//nums[i])*nums[i-1]
                ans.append(prefix)
               
        return ans