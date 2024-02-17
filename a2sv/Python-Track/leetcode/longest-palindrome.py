class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans=0
        odd=0
        c=0
        count=Counter(s)
        for num in count:
            if count[num]%2==0:
                ans+=count[num]
            else:
                odd+=count[num]
                c+=1
        if c:
            return ans+odd-(c-1)
        return ans
