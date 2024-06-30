# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        binary=bin(n)[2:]
        temp="0"*(32-len(binary))+binary
        for i in range(32):
            if temp[31-i]=="1":
                ans+=(2**(31-i))
        return ans