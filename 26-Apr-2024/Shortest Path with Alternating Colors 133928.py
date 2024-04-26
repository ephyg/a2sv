# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # red=true
        # blue=false
        graph=defaultdict(list)
        for x,y in redEdges:
            graph[x].append((y,True))
        for x,y in blueEdges:
            graph[x].append((y,False))

        def neighbours(node,col):
            neigh=[]
            for num,color in graph[node]:
                if col==color:
                    neigh.append((num,not col))
            return neigh

        queue=deque([(0,True,0),(0,False,0)])
        result=defaultdict(lambda :float("inf"))
        visited=set()
        while queue:
            node,color,cost=queue.popleft()
            result[node]=min(result[node],cost)
            neighbour=neighbours(node,color)
            for num,col in neighbour:
                if (num,col) not in visited:
                    queue.append((num,col,cost+1))
                    visited.add((num,col))

        ans=[]
        for i in range(n):
            if result[i]==float("inf"):
                ans.append(-1)
            else:
                ans.append(result[i])
        return ans