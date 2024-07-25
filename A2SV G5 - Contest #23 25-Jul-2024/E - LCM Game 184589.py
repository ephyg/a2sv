# Problem: E - LCM Game - https://codeforces.com/gym/532814/problem/E

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

    def lcm(a, b):
        return (a*b)//gcd(a, b)

    if n < 3:
        return n
    if n % 2:
        return lcm(lcm(n, n-1), n-2)
    else:
        if n == 3:
            return 6
        w = lcm(lcm(n, n-1), n-3)
        x = lcm(lcm(n, n-2), n-3)
        y = lcm(lcm(n-1, n-2), n-3)
        z = lcm(lcm(n, n-1), n-2)

        return max(w, x, y, z)


t = 1
for _ in range(t):
    print(solve())
