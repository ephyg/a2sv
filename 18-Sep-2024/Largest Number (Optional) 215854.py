# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                first = int(nums[i]+nums[j])
                second = int(nums[j]+nums[i])
                if second > first:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int("".join(nums)))


