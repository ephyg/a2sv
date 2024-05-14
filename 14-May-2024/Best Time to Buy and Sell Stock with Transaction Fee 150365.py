# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(idx,buy):
            if idx >= len(prices):
                return 0
            if buy:
                return max( dp(idx+1,False)- fee + prices[idx], dp(idx+1,buy))
            
            return max(-prices[idx] + dp(idx,True), dp(idx+1,buy))

        return dp(0,False)
            
                
           
        