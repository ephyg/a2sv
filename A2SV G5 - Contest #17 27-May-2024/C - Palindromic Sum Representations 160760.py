# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

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
    

palindromes=[int(i) for i in range(1,40005) if str(i)==str(i)[::-1]]
mod=10**9+7
dp=[0]*(40002)
dp[0]=1
for num in palindromes:
    for j in range(40002):
        if j-num>=0:
            dp[j]+=(dp[j-num])
            dp[j]%=mod

t = iinp()
for _ in range(t):
    n=iinp()
    print(dp[n])
