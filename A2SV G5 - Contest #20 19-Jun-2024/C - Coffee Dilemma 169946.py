# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

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
    tot=0
    for num in nums:
        tot+=num
        heappush(heap,num)
        while tot<0:
            tot-=heappop(heap)
    print(len(heap))
t = 1
for _ in range(t):
    solve()

# def main():
#     pass

# if __name__ == '__main__':

#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()