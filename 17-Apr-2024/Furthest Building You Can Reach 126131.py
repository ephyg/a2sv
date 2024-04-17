# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap=[]
        ans=0
        for i in range(1,len(heights)):
            diff=heights[i]-heights[i-1]
            if diff>0:
                if bricks>=diff:
                    bricks-=diff
                    heappush(max_heap,-diff)
                elif ladders>0:
                    if max_heap:
                        if diff >= -max_heap[0]:
                            ladders-=1
                        else:
                            ladders -= 1
                            bricks += -heapreplace(max_heap,-diff)-diff
                    else:                   
                        ladders-=1
                else:
                    return ans
            ans+=1
        return ans

                
        