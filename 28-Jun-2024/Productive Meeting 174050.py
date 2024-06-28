# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import sys, threading
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

def solve():
    n = iinp()
    nums = liinp()
    heap=[]
    for i in range(n):
        if nums[i] != 0:
            heappush(heap, (-nums[i], i+1))

    ans = []
    while len(heap) > 1:
        num1,idx1=heappop(heap)
        num2,idx2=heappop(heap)

        if num1<0 and num2<0:
            num1,num2 = num1+1,num2+1
            ans.append((idx1,idx2))
            
        if num1<0:
            heappush(heap, (num1, idx1))
        if num2<0:
            heappush(heap, (num2, idx2))
    count=len(ans)
    print(count)
    for x,y in ans:
        print(x,y)
t = iinp()
for _ in range(t):
    solve()

