class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, best = 0, len(nums) - 1, float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            best = min(best, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return best
