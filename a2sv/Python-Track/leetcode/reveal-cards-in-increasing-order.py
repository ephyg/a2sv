class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans=[]
        for i in range(len(deck)):
            ans.append(deck[i])
            if len(ans)>1:
                x=ans.pop(0)
                ans.insert(-1,x)
        return ans[::-1]
