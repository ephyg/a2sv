class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for bracket in s:
            if not stack:
                stack.append(bracket)
            else:
                if bracket==")" and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(bracket)
        return len(stack)