# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ans=[]
        visited=set()
        def bfs(num):
            queue=deque([num])
            count=1
            
            while queue:
                node=queue.popleft()
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
                        count+=1

            ans.append(count)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                bfs(i)

        res=0
        for num in ans:
            res+=(num*(n-num))
            n-=num

        return res
