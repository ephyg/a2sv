class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=list(set(nums))
        x.sort()
        nums[:len(nums)]=x
        return len(nums)