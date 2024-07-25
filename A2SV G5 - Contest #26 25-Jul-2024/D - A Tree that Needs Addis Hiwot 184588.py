# Problem: D - A Tree that Needs Addis Hiwot - https://codeforces.com/gym/537362/problem/D

import sys
import threading
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
    nums =[0]+liinp()
    graph = Counter(nums)

    childs = list(graph.values())
    childs.sort(reverse=True)

    for i in range(len(childs)):
        childs[i]-=len(childs)-i

    childs.sort(reverse=True)

    operation = len(childs)

    while childs[0]>0:
        for i in range(len(childs)):
            if childs[i]>0:
                childs[i]-=1
        childs[0]-=1
        operation+=1
        childs.sort(reverse=True)

    print(operation)


t = iinp()
for _ in range(t):
    solve()
