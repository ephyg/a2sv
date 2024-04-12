# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nums=[0]*len(graph)
        stack=[]
        visited=set()

        for i,num in enumerate(graph):
            if num and num[0] not in visited:
                nums[i]=1
                stack.append(i)

            while stack:
                node=stack.pop()

                for neighbour in graph[node]:
                    if nums[neighbour]==nums[node]:
                        return False
                        
                    if neighbour not in visited:
                        nums[neighbour]=2 if nums[node]==1 else 1

                        stack.append(neighbour)
                    visited.add(node)
        return True

