# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=0
        totalSum=sum(nums)
        for i  in range(len(nums)):
            rightSum=totalSum-leftSum-nums[i]
            if rightSum==leftSum:
                return i
            else:
                leftSum+=nums[i]
        return -1