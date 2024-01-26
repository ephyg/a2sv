class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left=0
        right=0
        ans=[]
        while right<len(secondList) and left<len(firstList):
            fx=firstList[left][0]
            fy=firstList[left][1]
            sx=secondList[right][0]
            sy=secondList[right][1]
            if (fx<=sy and fy>=sx) or (fx>=sy and fy<=sx):
                x=max(fx,sx)
                y=min(fy,sy)
                ans.append([x,y])
            if sy>=fy:
                left+=1
            else:
                right+=1
                
        return ans
                
                
