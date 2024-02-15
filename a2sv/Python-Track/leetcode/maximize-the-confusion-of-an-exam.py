class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dict=defaultdict(int)
        ans=0
        l,r=0,0
        while r<len(answerKey):
            while min(dict["T"],dict["F"])<=k and r<len(answerKey):
                dict[answerKey[r]]+=1
                if k>=min(dict["F"],dict["T"]):
                    ans=max(ans,r-l+1)
                r+=1
            while min(dict["T"],dict["F"])>k:
                dict[answerKey[l]]-=1
                l+=1
        return ans

                
                
