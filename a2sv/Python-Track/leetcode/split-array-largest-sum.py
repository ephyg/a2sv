class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def validate(limit):
            count=1
            tot=0
            for i in range(len(nums)):
                tot+=nums[i]
                if tot>limit:
                    count+=1
                    tot=nums[i]
            return count
                    
        left,right,best=max(nums),sum(nums),float("inf")
        
        while left<=right:
            mid=left+(right-left)//2
            x=validate(mid)
            if x<=k:
                best=mid
                right=mid-1
            else:
                left=mid+1
        return best
