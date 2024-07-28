# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans=False
        def additive(idx,curr):
            nonlocal ans
            if ans:
                return
            if len(curr)>2 and curr[-2]+curr[-3]!=curr[-1]:
                return 
            if idx>=len(num):
                if len(curr)>2:
                    ans=True
                    return
                else:
                    ans=False
                    return
            for i in range(idx,len(num)):
                if len(num[idx:i+1])>1 and num[idx:i+1][0]=='0':
                    continue
                n=int(num[idx:i+1])
                curr.append(n)
                additive(i+1,curr)
                curr.pop()
        additive(0,[])
        return ans
                    
