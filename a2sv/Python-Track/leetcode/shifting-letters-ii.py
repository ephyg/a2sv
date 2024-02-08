class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefixSum=[0]*(len(s)+1)
        for f,e,d in shifts:
            if d==0:
                prefixSum[f]-=1
                prefixSum[e+1]+=1
            else:
                prefixSum[f]+=1
                prefixSum[e+1]-=1
        for i in range(1,len(prefixSum)):
            prefixSum[i]=prefixSum[i-1]+prefixSum[i]
        ans=[]
        alphabet="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            idx=ord(s[i])-ord('a')
            key=(idx+prefixSum[i])%26
            ans.append(alphabet[key])
        
        return "".join(ans)
            
                