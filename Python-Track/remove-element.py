class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=nums.count(val)
        for i in range(x):
            nums.remove(val)
        return len(nums)