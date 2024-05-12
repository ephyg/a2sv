# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xx=bin(n)[2:]
        for i in range(1,len(xx)):
            if xx[i-1]==xx[i]:
                return False
        return True