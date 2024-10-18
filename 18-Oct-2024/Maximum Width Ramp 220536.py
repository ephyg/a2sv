# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        stack = []
        for i in range(len(nums)):
            if not stack or stack[-1][0]>nums[i]:
                stack.append((nums[i],i))
        
        width = 0
        print(stack)
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1][0] <= nums[i]:
                width = max(width,i-stack[-1][1])
                stack.pop()
        return width