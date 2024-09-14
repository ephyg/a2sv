# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # nums = [1,2,3,3,2,2]
        max_ = max(nums)
        
        left = 0
        ans = 1
        while left < len(nums):
            count = 0
            while left < len(nums) and nums[left]==max_:
                count += 1
                left += 1
            left += 1
            ans = max(count,ans)
        return ans
