# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        max_=-1
        degree=[0]*len(edges)
        visit=[False]*len(edges)
        for i in range(len(edges)):
            degree[edges[i]]+=1 if edges[i]!=-1 else 0
        
        queue=deque()
        for i in range(len(edges)):
            if degree[i]==0:
                queue.append(i)

        while queue:
            node=queue.popleft()
            visit[node]=True
            if edges[node]!=-1:
                degree[edges[node]]-=1
                if degree[edges[node]]==0:
                    queue.append(edges[node])

        for i in range(len(edges)):
            if not visit[i]:
                count=1
                visit[i]=True
                neigh=edges[i]
                while not visit[neigh]:
                    count+=1
                    visit[neigh]=True
                    neigh=edges[neigh]
                max_=max(count,max_)



        return max_

