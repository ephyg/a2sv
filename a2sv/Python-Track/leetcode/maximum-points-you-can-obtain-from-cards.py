class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=k
        right=len(cardPoints)-k
        merge=cardPoints[right:]+cardPoints[:left]
        tot=sum(merge[:k])
        ans=tot
        for i in range(1,len(merge)-k+1):
            tot+=merge[i+k-1]-merge[i-1]
            ans=max(tot,ans)
        return ans
