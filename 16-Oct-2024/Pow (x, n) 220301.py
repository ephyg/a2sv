# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:

        base = x
        answer = 1

        isNegative = False
        if n < 0:
            isNegative =  True
            n = 0 - n
        while n:
            if n&1:
                answer *= base
            base *= base
            n >>= 1

        if isNegative:
            return 1 / answer
            
        return answer