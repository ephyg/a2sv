# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        def inrange(num):
            return (1 <= num <= 6)
        tot = sum(rolls)
        distribute = mean * (n + len(rolls)) - tot
        
        if not ( 0 < distribute <= n*6) or distribute < n:
            return []
        num = distribute // n
        remaining = distribute % n
        ans = [num + 1] * remaining

        for i in range(n - len(ans)):
            ans.append(num)
        return ans
