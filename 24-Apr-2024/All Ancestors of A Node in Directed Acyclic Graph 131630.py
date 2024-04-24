# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for x, y in edges:
            graph[x].append(y)
            degree[y] += 1

        result = defaultdict(list)
        queue = deque()
        for i in range(n):
            if degree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                temp=[node]
                temp.extend(result[node])
                temp.extend(result[neighbour])
                result[neighbour]=sorted(list(set(temp)))
                degree[neighbour]-=1
                if degree[neighbour]==0:
                    queue.append(neighbour)
        ans=[]
        for i in range(n):
            ans.append(result[i])
        return ans
