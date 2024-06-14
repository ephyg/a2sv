# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        op="+-/*"
        s.strip()
        char=[]
        i=0
        for j,ch in enumerate(s):
            if ch in op:
                char.append(int(s[i:j]))
                char.append(ch)
                i=j+1
        char.append(int(s[i:]))
        stack=[]
        flag=False
        for num in char:
            if flag:
                operation=stack.pop()
                x=stack.pop()
                if operation=="/":
                    stack.append(x//num)
                else:
                    stack.append(x*num)
                flag=False
                continue
            if not str(num).isnumeric() and num in "/*":
                flag=True
            stack.append(num)
        res=[]
        flag=False
        for num in stack:
            if flag:
                operation=res.pop()
                x=res.pop()
                if operation=="+":
                    res.append(x+num)
                else:
                    res.append(x-num)
                flag=False
                continue

            if not str(num).isnumeric():
                flag=True
            res.append(num)
        return res[0]