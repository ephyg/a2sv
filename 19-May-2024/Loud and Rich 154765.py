# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        graph=defaultdict(list)
        indegree=[0]*n
        for u,v in richer:
            graph[u].append(v)
            indegree[v]+=1
    
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
                
        answer=[int(i) for i in range(n)]
        while queue:
            node=queue.popleft()
            for neigh in graph[node]:
                indegree[neigh]-=1
                
                if quiet[answer[node]]<quiet[answer[neigh]]:
                    answer[neigh]=answer[node]
                if indegree[neigh]==0:
                    queue.append(neigh)
        # print(answer)
        return answer


