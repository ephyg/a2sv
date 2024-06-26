# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        nums=[1,1]
        for i in range(2,n+1):
            nums.append(nums[i-2]+nums[i-1])
        return nums[-1]