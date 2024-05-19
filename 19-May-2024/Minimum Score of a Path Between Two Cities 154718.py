# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)

        for i in range(len(roads)):
            graph[(roads[i][0])].append((roads[i][1],roads[i][2]))
            graph[(roads[i][1])].append((roads[i][0],roads[i][2]))
        
        queue=deque([(1,float("inf"))])
        visited={1}
        min_=float("inf")
        while queue:
            bound=len(queue)
            for i in range(bound):
                node,dist=queue.popleft()
                min_=min(dist,min_)
                for neigh in graph[node]:
                    min_=min(neigh[1],min_)
                    if not neigh[0] in visited:
                        visited.add(neigh[0])
                        queue.append((neigh[0],neigh[1]))
        return min_
                





        return 2