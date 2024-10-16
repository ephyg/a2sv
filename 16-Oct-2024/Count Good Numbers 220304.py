# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9 + 7)
        ans = 1
        q,r = n//2, n%2

        ans *= pow(4,q,mod)
        ans *= pow(5,q,mod) * pow(5,r,mod)
        return ans % mod