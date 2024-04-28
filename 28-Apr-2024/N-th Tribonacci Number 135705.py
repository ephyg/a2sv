# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        tot=2
        if n==a:
            return a
        if n==1:
            return b
        if n==2:
            return c
        
        while n-3>0:
            temp=tot
            a=b
            b=c
            c=tot
            tot=a+b+c
            n-=1
        return a+b+c
