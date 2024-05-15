# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}

        def dp(row,col):
            if not (0<=row<m and 0<=col<n):
                return 0
            if (row,col)==(m-1,n-1):
                return 1
            if (row,col) not in memo:
                memo[(row,col)]=dp(row,col+1)+dp(row+1,col)
            return memo[(row,col)]
        return dp(0,0)