# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        max_=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i]>max_:
                max_=prices[i]
            else:
                ans=max(ans,max_-prices[i])
        return ans