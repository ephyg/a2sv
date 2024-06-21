# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            var = nums[-1]
            nums.pop()
            nums.insert(0, var)
        return nums