class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right,check=0,len(nums)-1,False
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                check=True
                break
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if check:
            return bisect_right(nums,target)-1
        return bisect_right(nums,target)