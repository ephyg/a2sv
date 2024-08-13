# Problem: Remove Duplicates from Sorted Array
(Easy) - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=list(set(nums))
        x.sort()
        nums[:len(nums)]=x
        return len(nums)