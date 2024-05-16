# Problem: E - XOR Fan - https://codeforces.com/gym/522079/problem/E

import sys
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
    
    
    
def solve(n,nums,s,q):
    prefix=[0]
    ones=0
    zeros=0
    for i in range(n):
        prefix.append(prefix[i]^nums[i])
        if s[i]=="0":
            zeros^=nums[i]
        else:
            ones^=nums[i]
    ans=[]
    for i in range(q):
        query=liinp()
        if query[0]==2:
            if query[1]==1:
                ans.append(ones)
            else:
                ans.append(zeros)
        else:
            x,l,r=query
            num=prefix[r]^prefix[l-1]
            ones^=num
            zeros^=num
    print(*ans)

t = iinp()
for _ in range(t):
    n=iinp()
    nums=liinp()
    s=sinp()
    q=iinp()
    solve(n,nums,s,q)