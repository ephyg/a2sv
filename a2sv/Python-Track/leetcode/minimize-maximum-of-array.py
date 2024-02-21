class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_=nums[0]
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        for i in range(1,len(nums)):
            if nums[i]>nums[0]:
                calc=ceil((prefix[i])/(i+1))
                max_=max(calc,max_)
                print(calc,max_)
        return max_