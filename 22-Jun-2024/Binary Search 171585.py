# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        while left<=right:
            middle=(right+left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            else:
                left=middle+1
        return -1