# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # @cache
        # def rec(left,right):
        #     if left==right:
        #         return piles[right]
        #     leftNum=piles[left]-rec(left+1,right)
        #     rightNum=piles[right]-rec(left,right-1)
        #     max_=max(leftNum,rightNum)
        #     return max_

        # if rec(0,len(piles)-1)>=0:
        #     return True
        # return False

        # or 
        return True
        
