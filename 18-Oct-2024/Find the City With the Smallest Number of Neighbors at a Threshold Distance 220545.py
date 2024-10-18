# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], d: int
    ) -> int:

        matrix = [[float("inf")] * n for i in range(n)]
        for i in range(n):
            matrix[i][i] = 0

        for u,v,w in edges:
            matrix[u][v] = matrix[v][u] = w

        for i in range(n):
            for r in range(n):
                for c in range(n):
                    if matrix[i][c]!=float("inf") and matrix[r][i] != float("inf"):
                        matrix[r][c] = min(matrix[i][c]+matrix[r][i],matrix[r][c])
        num = float("inf")
        idx = -1
        for r in range(n):
            count = 0
            for c in range(n):
                if matrix[r][c] <= d:
                    count += 1
            if count <= num:
                num = count
                idx = r

        return idx
            
