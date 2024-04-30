# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        degree=[0]*n
        for x,y in edges:
            graph[x].append(y)
            degree[y]+=1
        
        res=[]
        for i in range(n):
            if degree[i]==0:
                res.append(i)
        
        if len(res)==1:
            return res[0]
        else:
            return -1
        
