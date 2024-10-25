# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        LPS = [0]*n

        left,right = 0,1
        while right < n  and left < n:
            if needle[left] == needle[right]:
                LPS[right] = left + 1
                left += 1
                right += 1
            else:
                if  left == 0:
                    right += 1
                else:
                    left = LPS[left -1]
        left,right = 0,0
        while left < n and right < len(haystack) :
            if needle[left] == haystack[right]:
                left += 1
                right += 1
            else:
                if left == 0:
                    right += 1
                else:
                    left = LPS[left -1]
            if left >= n:
                return right - n
        return -1