class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op="+*-/"
        for i in range(len(tokens)):
            if tokens[i] in op:
                if len(stack)>=2:
                    calc=int(eval(f"{stack[-2]} {tokens[i]} {stack[-1]}"))
                    stack.pop()
                    stack.pop()
                    stack.append(calc)
            else:
                stack.append(tokens[i])
        return int(stack[-1])