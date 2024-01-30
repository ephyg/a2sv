class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        l=0
        r=k
        ans=0
        count=Counter(s[l:k])
        for i in count:
            if i in v:
                ans+=count[i]
        temp=ans
        while r<len(s):
            print(ans,temp)
            if s[l] in v:
                temp-=1
            if s[r] in v:
                temp+=1
            ans=max(temp,ans)
            l+=1
            r+=1
        return ans
                
                
