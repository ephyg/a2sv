# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo={}
        def dp(num):
            if num==1:
                return 1
                
            if num not in memo:   
                ans=0
                for i in range(1,num):
                    ans=max(ans,(num-i)*(i),(num-i)*dp(i),dp(num-i)*(i))
                memo[num]=ans
            return memo[num]
        return dp(n)