# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo={}
        exist = set(stones)
        if stones[1]-stones[0]>1:
            return False

        def dp(num,k):
            if stones[-1]==num:
                return True
            if num==0:
                return dp(num+k,k)
            if num not in exist or k==0:
                return False

            if (num,k) not in memo:
                memo[(num,k)]=dp(num+k+1,k+1) or dp(num+k,k) or dp(num+k-1,k-1)         
            return memo[(num,k)]
        return dp(0,1)