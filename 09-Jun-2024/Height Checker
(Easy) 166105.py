# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums=sorted(heights)
        count=0
        for i in range(len(nums)):
            if nums[i]!=heights[i]:
                count+=1
        return count

