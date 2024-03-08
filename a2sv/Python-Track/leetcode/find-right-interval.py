class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:        
        start=sorted([(intervals[i][0],i) for i in range(len(intervals))])
        ans=[]
        for i,num in enumerate(intervals):
            left=bisect_left(start,(num[1],0))
            if left<len(intervals) and intervals[start[left][1]][0]>=num[1]:
                ans.append(start[left][1])
                continue
            ans.append(-1)
        return ans
           

        