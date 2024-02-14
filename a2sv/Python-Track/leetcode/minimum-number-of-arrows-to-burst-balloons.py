class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count=1
        i,j=points[0][0],points[0][1]
        for k in range(1,len(points)):
            x=points[k][0]
            y=points[k][1]

            if j>=x:
                i,j=max(i,x),min(j,y)
            else:
                i,j=x,y
                count+=1
        return count