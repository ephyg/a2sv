# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=set()
        def backtrack(idx,candidates):
            if len(candidates)==len(s):
                ans.add(candidates[:])
                return 
                
            for i in range(idx,len(s)):
                if s[i].isalpha():
                    x=candidates+s[idx].lower()
                    backtrack(i+1,x)
                    y=candidates+s[idx].upper()
                    backtrack(i+1,y)
                else:
                    backtrack(i+1,candidates+s[i])
        backtrack(0,"")
        return ans
                    

    