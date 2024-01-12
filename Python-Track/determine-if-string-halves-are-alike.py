class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        res=0
        vowels={'a','i','e','o','u','A','E','I','O','U'}
        for i in range(len(s)//2):
            if s[i] in vowels:
                res+=1
            if s[len(s)-1-i] in vowels:
                res-=1
        return res==0