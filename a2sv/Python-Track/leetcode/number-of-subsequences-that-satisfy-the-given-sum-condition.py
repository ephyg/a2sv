class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod=10**9 + 7
        if nums[0]>target:
            return 0
        ans=0
        left=0
        right=len(nums)-1
        while left<=right:
            a,b=nums[left],nums[right]
            if a+b<=target:
                ans+=pow(2,right-left,mod)
                left+=1
            else:
                right-=1
        return ans%mod