# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=set(nums)
        if(len(x)==len(nums)):
            return False
        else:
            return True
        