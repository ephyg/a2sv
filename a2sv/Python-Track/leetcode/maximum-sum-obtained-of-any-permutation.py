class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        mod=10**9 + 7
        ls=[0]*(len(nums)+1)
        for i,num in enumerate(requests):
            ls[num[0]]+=1
            ls[num[1]+1]-=1
        prefix=list(accumulate(ls[:-1]))
        prefix.sort()
        tot=0

        for i in range(len(nums)):
            tot+=(nums[i]*prefix[i])
        

        return tot%mod

