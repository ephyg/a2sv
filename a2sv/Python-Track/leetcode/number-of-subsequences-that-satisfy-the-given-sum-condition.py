class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod=10**9 + 7
        ans=0
        for i in range(len(nums)):
            bisect=bisect_right(nums,target-nums[i])-1
            if bisect<i:
                break
            ans+=(pow(2,bisect-i,mod))
        return ans%mod