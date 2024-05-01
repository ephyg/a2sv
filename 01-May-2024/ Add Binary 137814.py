# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        ans=x+y
        return str(bin(ans))[2:]