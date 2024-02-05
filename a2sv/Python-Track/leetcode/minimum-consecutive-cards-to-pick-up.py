class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards))==len(cards):
            return -1
        dic=defaultdict(int) 
        _min=float("inf")
        for i in range (len(cards)):
            if cards[i] in dic:
                if _min>(i-(dic[cards[i]])):
                    _min=(i-dic[cards[i]])                
            dic[cards[i]]=i
        if _min==float("inf"):
            return -1
        return _min+1
