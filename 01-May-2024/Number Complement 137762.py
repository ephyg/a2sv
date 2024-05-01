# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        i=0
        tot=0
        while num:
            if (num%2)==0:
                tot+=(2**i)
            num>>=1
            i+=1

        return tot