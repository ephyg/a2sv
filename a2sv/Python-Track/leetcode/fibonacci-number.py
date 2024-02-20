class Solution:
    
    def fib(self, n: int, m={}) -> int:
        if n in m:
            return m[n]
        if n<=1:
            return n
        ans = (self.fib(n-1, m)+self.fib(n-2, m))
        m[n] = ans

        return ans
