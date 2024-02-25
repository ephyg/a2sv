class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        ans=0
        for bracket in s:
            if bracket=="(":
                stack.append(ans)
                ans=0
            else:
                x=stack.pop()
                ans=max(1,ans*2)+x
        return ans