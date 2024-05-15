# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dp(idx,n):
            if n<0 or idx>=len(coins):
                return 0
            if n==0:
                return 1
            if (idx,n) not in memo:
                memo[(idx,n)]=dp(idx,n-coins[idx])+dp(idx+1,n)
            return memo[(idx,n)]
        return dp(0,amount)