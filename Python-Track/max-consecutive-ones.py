class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp=0
        left=0
        right=0
        while right<len(nums):
            if(nums[right]==1):
                right+=1
                temp=max(temp,len(nums[left:right]))
            else:
                temp=max(temp,len(nums[left:right]))
                right+=1
                left=right
        return temp
                           
                
    