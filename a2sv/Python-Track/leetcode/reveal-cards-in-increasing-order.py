class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans=[]
        for i in range(len(deck)):
            ans.insert(0,deck[-1-i])
            if len(ans)>1:
                x=ans.pop()
                ans.insert(1,x)
        return ans
