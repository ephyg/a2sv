# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix)
        dp=[[0]*(m+2) for i in range(n+1)]

        for i in range(1,m+1):
            dp[1][i]=matrix[0][i-1]
        for i in range(n+1):
            dp[i][0]=float("inf")
            dp[i][m+1]=float("inf")

        for r in range(2,n+1):
            for c in range(1,m+1):
                dp[r][c]+=min(dp[r-1][c-1],dp[r-1][c],dp[r-1][c+1])+matrix[r-1][c-1]
        return min(dp[n])

            


