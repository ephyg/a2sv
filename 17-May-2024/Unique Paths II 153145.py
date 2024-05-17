# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo={}
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])

        dp=[[0]*(m+1) for i in range(n+1)]
        dp[0][1]=1

        for r in range(1,n+1):
            for c in range(1,m+1):
                if obstacleGrid[r-1][c-1]==0:
                    dp[r][c]=dp[r-1][c]+dp[r][c-1]
                
        return dp[n][m]

        # top down approach
        # def dp(row,col):
        #     if not (0<=row<m and 0<=col<n):
        #         return 0
        #     if obstacleGrid[row][col]==1:
        #         return 0
        #     if (row,col)==(m-1,n-1):
        #         return 1
        #     if (row,col) not in memo:
        #         memo[(row,col)]=dp(row,col+1)+dp(row+1,col)
        #     return memo[(row,col)]
        # return dp(0,0)