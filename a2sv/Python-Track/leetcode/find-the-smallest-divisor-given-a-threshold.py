class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right,best=1,sum(nums),-1
        def validate(limit):
            count=0
            for num in nums:
                count+=ceil(num/limit)
            return count
        while left <= right:
            mid=left+(right-left)//2
            minThreshold=validate(mid)
            if minThreshold<=threshold:
                best=mid
                right=mid-1
            else:
                left=mid+1
        return best