# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=defaultdict(int)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[b]+=1
            indegree[a]+=1
        
        queue=deque()
        for i in range(n):
            if indegree[i]==1:
                queue.append(i)

        while queue:
            if n <= 2:
                return queue
            for i in range(len(queue)):
                n-=1
                node=queue.popleft()
                for neigh in graph[node]:
                    indegree[neigh]-=1
                    if indegree[neigh]==1:
                        queue.append(neigh)
        return [0]


