# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(list(allowed))
        count = 0
        def checker(word):
            for char in word:
                if char not in allow:
                    return False
            return True
            
        for word in words:
            count += checker(word)
        return count