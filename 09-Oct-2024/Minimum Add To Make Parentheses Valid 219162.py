# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        closing = 0

        for bracket in s:
            if bracket == "(":
                opening += 1
            elif bracket == ")" and opening == 0:
                closing += 1
            else:
                opening -= 1
        return opening + closing
                