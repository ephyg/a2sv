# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        
        d=2
        nums=set()
        while d*d<=n:
            while n%d==0:
                nums.add(d)
                n//=d
            d+=1
        if n>1:
            nums.add(n)
        
        for num in nums:
            if not num in [2,3,5]:
                return False
        return True

