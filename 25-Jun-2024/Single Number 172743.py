# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z=list(set(nums))
        for i in range(len(z)):
            x=nums.count(z[i])
            if(x==1):
                return z[i]