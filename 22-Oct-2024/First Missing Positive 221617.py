# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] <=0 or nums[i] > len(nums):
                nums[i] = len(nums)+1
        nums.append(len(nums)+1)
        # print(nums)
        for i in range(len(nums)):
            while  nums[i]-1!= nums[nums[i]-1]-1:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp


        for i in range(1,len(nums)):
            if i!=nums[i-1]:
                return i
        return len(nums) 

