class Solution:
    def isValid(self, s: str) -> bool:
        my_dict={"(":")","[":"]","{":"}"}
        stack=[]
        for i in range(len(s)):
            if s[i] in my_dict:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                x=stack.pop()
                if my_dict[x]!=s[i]:
                    return False
        return len(stack)==0
