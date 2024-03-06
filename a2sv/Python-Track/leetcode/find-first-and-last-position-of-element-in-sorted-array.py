class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        lbisect,rbisect=-1,-1
        ans=False
        while left<=right:
            mid=left+(right-left)//2
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                ans=True
                break
        if ans:
            lbisect=bisect_left(nums,target)
            rbisect=bisect_right(nums,target)-1
        return [lbisect,rbisect]