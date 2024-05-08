# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

import sys
from collections import defaultdict, Counter, deque
from math import ceil, gcd, sqrt
from heapq import heapify, heappop, heapreplace, heappush
from bisect import bisect_right, bisect_left
    

# 0 0 // 15-9szssssssssss
# _ _
    
def solve(m,s):
    original=s
    ans=[]
    for i in range(m):
        if s>=9:
            ans.append(9)
            s-=9
        elif s<9:
            ans.append(s)
            s-=s

    if sum(ans)!=original:
        print(-1,-1)
        return
    ans=[str(i) for i in ans]
    num=str(int("".join(ans)))
    if len(ans)!=len(num):
        print(-1,-1)
        return
    ans=[int(i) for i in ans]
    min_=ans[::-1]
    # print(min_)
    if min_[0]==0:
        for i in range(1,m):
            if min_[i]>0:
                min_[i]-=1
                min_[0]=1
                break
    min_=[str(i) for i in min_]
    print(str(int("".join(min_))),num)
    

            

        
    
m,s = list(map(int, sys.stdin.readline().strip().split()))
# for _ in range(t):
solve(m,s)