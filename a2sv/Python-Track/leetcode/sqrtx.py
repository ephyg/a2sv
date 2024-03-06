class Solution:
    def mySqrt(self, x: int) -> int:
        left,right,best=0,x,0
        while right>=left:
            mid=left+(right-left)//2
            if (mid*mid)<=x:
                best=max(mid,best)
                left=mid+1
            elif (mid*mid)>x:
                right=mid-1
        return best
