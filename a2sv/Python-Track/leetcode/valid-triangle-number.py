class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans=0
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                tot=nums[left]+nums[right]
                if tot>nums[i]:
                    ans+=right-left
                    left+=1
                else:
                    right-=1
        return ans