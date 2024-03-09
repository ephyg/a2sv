class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters=list(set(heaters))
        heaters.sort()
        ans=0
        for i,num in enumerate(houses):
            bisect=bisect_left(heaters,num)
            if bisect==0:
                temp=abs(heaters[bisect]-num)
                ans=max(ans,temp)
            elif bisect==len(heaters):
                temp=abs(heaters[bisect-1]-num)
                ans=max(ans,temp)
            else:
                tempLeft=abs(heaters[bisect-1]-num)
                tempRight=abs(heaters[bisect]-num)
                ans=max(min(tempLeft,tempRight),ans)
        return ans
