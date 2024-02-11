class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        prefix=0
        ans=[]
        for i,num in enumerate(nums):
            prefix+=nums[i]
            leftSide=(i+1)*num -prefix
            rightSide=(total-prefix)-(len(nums)-i-1)*num
            ans.append(leftSide+rightSide)
        return ans