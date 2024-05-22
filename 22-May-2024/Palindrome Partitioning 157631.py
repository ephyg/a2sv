# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            return word==word[::-1] and len(word)>0

        ans=[]
        def backtrack(idx,curr):
            if idx>=len(s):
                ans.append(curr[:])
                return          
            for i in range(idx,len(s)):
                if isPalindrome(s[idx:i+1]):
                    curr.append(s[idx:i+1])
                    backtrack(i+1,curr)
                    curr.pop()
        backtrack(0,[])
        return ans

