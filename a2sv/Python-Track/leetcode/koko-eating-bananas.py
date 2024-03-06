class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(k):
            hour=0
            for i,num in enumerate(piles):
                hour+=ceil(num/k)
            return hour
        left,right,best=1,max(piles),float("inf")
        while left<=right:
            mid=left+(right-left)//2
            if validate(mid)<=h:
                best=mid
                right=mid-1
            else:
                left=mid+1
        return best