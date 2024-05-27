# Problem: D -  Longest Good Sequence - https://codeforces.com/gym/524965/problem/D

import sys , threading
from collections import defaultdict, Counter, deque
from math import ceil, gcd, sqrt
from heapq import heapify, heappop, heapreplace, heappush
from bisect import bisect_right, bisect_left
    
def lsinp():
    return sys.stdin.readline().strip().split()
def liinp():
    return list(map(int, sys.stdin.readline().strip().split()))
def sinp():
    return sys.stdin.readline().strip()
def iinp():
    return int(sys.stdin.readline().strip())
    
def divisor(num):
    ans=set()
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            ans.add(i)
            ans.add(num//i)
    return list(ans)
    
def solve(n,nums):
    dp = [0] *(max(nums) + 1)
    
    for num in nums:
        factors=divisor(num)
        dp[num] = 1

        for div in factors:
            dp[num] = max(dp[num], dp[div] + 1)

        for div in factors:
            dp[div] = max(dp[div], dp[num])
    print(max(dp))    

t = 1
for _ in range(t):
    n=iinp()
    nums=liinp()
    solve(n,nums)
