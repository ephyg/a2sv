# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(points)):
            for  j in range(i+1,len(points)):
                x1,y1=points[i]
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y2-y1)
                graph[tuple(points[i])].append((dist,tuple(points[j])))
                graph[tuple(points[j])].append((dist,tuple(points[i])))
        
        queue=[(0,tuple(points[0]))]
        visited=set()
        ans=0
        count=0
        while queue and count<len(points):
            # print(queue)
            dist,node=heappop(queue)
            if node in visited:
                continue
            ans+=dist
            visited.add(node)
            for neigh in graph[(node)]:
                heappush(queue,(neigh[0],neigh[1]))
            count+=1
        return ans



