class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right,best=0,len(citations)-1,0

        while left <= right:
            mid=left+(right-left)//2
            diff=len(citations)-mid
            if citations[mid]>=diff:
                best=max(best,diff)
                right=mid-1
            else:
                left=mid+1
        return best


