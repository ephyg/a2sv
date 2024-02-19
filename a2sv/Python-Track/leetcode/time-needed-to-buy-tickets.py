class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count=0
        while tickets[k]!=0:
            for i, num in enumerate(tickets):
                if tickets[i]!=0:
                    tickets[i]-=1
                    count+=1
                if not tickets[k]:
                    break
        return count

        