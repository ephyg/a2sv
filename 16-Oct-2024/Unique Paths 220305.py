# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0]*(n+1) for i in range(m+1)]
        matrix[1][1] = 1

        for r in range(1,m+1):
            for c in range(1,n+1):
                if r==1 and c ==1:
                    continue
                matrix[r][c] = matrix[r-1][c]+matrix[r][c-1]
        return matrix[m][n]

