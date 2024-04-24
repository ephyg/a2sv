# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree=[0]*len(graph)
        neighbours=defaultdict(list)

        for i in range(len(graph)):
            for num in graph[i]:
                neighbours[num].append(i)
                outdegree[i]+=1
        queue=deque()
        for i,num in enumerate(outdegree):
            if num==0:
                queue.append(i)
        ans=[]
        while queue:
            node=queue.popleft()
            ans.append(node)

            for neighbour in neighbours[node]:
                outdegree[neighbour]-=1
                if outdegree[neighbour]==0:
                    queue.append(neighbour)
        return sorted(ans)
                    

            
