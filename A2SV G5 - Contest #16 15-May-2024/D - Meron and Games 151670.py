# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

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

def main():
    n=iinp()
    nums=liinp()
    freq=Counter(nums)
    memo = {}
    max_ = max(freq)
    def dp(num):
        if num > max_:
            return 0
        if num not in memo:
            memo[num] = max(freq[num]*num + dp(num+2), dp(num + 1))
        return memo[num]
    print(dp(min(freq)))
   

if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()