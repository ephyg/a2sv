# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

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

def main():
    def solve(nums):
        n, a, b, c = nums
        memo = defaultdict(int)
        def dp(x):
            if x == 0:
                return 0
            if x < 0 or (x > 0 and x < a and x < b and x < c):
                return float("-inf")
            if x not in memo:
                i = dp(x-a)
                j = dp(x-b)
                k = dp(x-c)
                memo[x] = max(i, j, k)+1
            return memo[x]
        print(dp(n))
    nums = liinp()
    solve(nums)
if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
