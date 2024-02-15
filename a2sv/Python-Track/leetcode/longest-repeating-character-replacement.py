class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freq=defaultdict(int)
        ans=0  
        while r<len(s):
            freq[s[r]]+=1

            while k<(r-l+1)-max(freq.values()):
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
    