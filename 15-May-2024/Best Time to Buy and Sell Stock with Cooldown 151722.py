# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=defaultdict(int)
        def dp(idx,buy):
            if idx >= len(prices):
                return 0
            if buy:
                if (idx,buy) not in memo:
                    memo[(idx,buy)] = max( dp(idx+2,False)+ prices[idx], dp(idx+1,buy))
                return memo[(idx,buy)]
            
            return max(-prices[idx] + dp(idx,True), dp(idx+1,buy))

        return dp(0,False)