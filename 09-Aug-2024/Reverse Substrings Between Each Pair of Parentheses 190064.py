# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i,char in enumerate(s):
            if char == "(" and  not stack:
                stack.append((char,i))
            else:
                if stack and stack[-1][0]=="(" and char == ")":
                    x= stack.pop()
                    temp = s[x[1]:i+1][::-1]
                    s = s[:x[1]]+temp +s[i+1:]
                elif char == "(":
                    stack.append((char,i))
        #     print(s)
        # print(s)
        ans=""
        for i in s:
            if i not in "()":
                ans+=i
        return ans

                    
            
                