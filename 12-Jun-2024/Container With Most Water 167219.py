# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx=0
        left=0
        right=len(height)-1
        while right>left:
            area=(right-left)*min(height[right],height[left])
            mx=max(area,mx)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return mx