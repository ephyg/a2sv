# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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
def primeFactors(n):
    factors = []
    if n == 1:
        return factors
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def solve(num,arr):
    factors=[]
    for n in arr:
        factors.extend(primeFactors(n))

    count=Counter(factors)
    for freq in count.values():
        if freq%num:
            return False
    return True

t = iinp()
for _ in range(t):
    num=iinp()
    arr=liinp()
    if solve(num,arr):
        print("YES")
    else:
        print("NO")
