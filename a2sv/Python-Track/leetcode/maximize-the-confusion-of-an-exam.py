class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        true,false=0,0
        ans=0
        l,r=0,0
        while r<len(answerKey):
            while min(true,false)<=k and r<len(answerKey):
                if answerKey[r] == "T" :
                    true+=1
                else: 
                    false+=1
                if k>=min(false,true):
                    ans=max(ans,r-l+1)
                r+=1
            while min(true,false)>k:
                if answerKey[l]=="T":
                    true-=1
                else:
                    false-=1
                l+=1
        return ans

                
                
