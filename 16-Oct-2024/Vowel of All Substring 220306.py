# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        for i, char in enumerate(word):
            if char in "aeiou":
                ans += (i+1) * (len(word)-i)  
        return ans
