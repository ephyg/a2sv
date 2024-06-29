# Problem: D - Binyam and Kalkidan - https://codeforces.com/gym/531455/problem/D

import sys, threading
from collections import defaultdict, Counter, deque
from math import ceil, factorial, gcd, prod, sqrt
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
    nums = sinp()
    ans=[]
    factorials={
        0:[],
        1:[],
        2:[2],
        3:[3],
        4:[2,2,3],
        5:[5],
        6:[5,3],
        7:[7],
        8:[7,2,2,2],
        9:[7,3,3,2]
    }
    for num in nums:
        ans.extend(factorials[int(num)])
    ans.sort(reverse=True)
    ans=[str(i) for i in ans]
    print("".join(ans))


t = 1
for _ in range(t):
    solve()

