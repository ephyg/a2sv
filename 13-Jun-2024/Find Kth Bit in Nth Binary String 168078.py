# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:     
        def inverse(s):
            s=[i for i in s]
            for i in range(len(s)):
                if s[i] == '0':
                    s[i] = '1'
                else:
                    s[i] = '0'
            s.reverse()
            return "".join(s)
            
        def generate(n):
            if n==1:
                return "0"
            return generate(n-1) + "1" + inverse(generate(n-1))
        return generate(n)[k-1]
