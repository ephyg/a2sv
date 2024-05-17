# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=len(s)+1
        n=len(t)+1
        dp=[[0]*(n) for i in range(m)]
        for i in range(n):
            dp[0][i]=1

        for r in range(1,m):
            for c in range(1,n):
                if s[r-1]==t[c-1]:
                    dp[r][c]=dp[r-1][c-1]
                else:
                    dp[r][c]=dp[r][c-1]
        return dp[m-1][n-1]

