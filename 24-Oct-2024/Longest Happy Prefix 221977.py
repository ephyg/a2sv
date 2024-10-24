# Problem: Longest Happy Prefix - https://leetcode.com/problems/longest-happy-prefix/description/

class Solution:
    def longestPrefix(self, s: str) -> str:
        
        LPS = [0]*len(s)
        left,right = 0,1
        
        while right < len(s) and left < len(s):
            if s[left] == s[right]:
                LPS[right] = left+1
                left += 1
                right += 1

            else:
                if left == 0:
                    right += 1
                else:
                    left = LPS[left - 1]

        ans = ""
        k = 0 
        for  i in range(LPS[-1],0,-1):
            ans += s[len(s)-1-k]
            k+=1
        return ans[::-1]