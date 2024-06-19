# Problem: D - The Equalizer XOR - https://codeforces.com/gym/528792/problem/D

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
    prefix=[nums[0]]
    for i in range(1,n):
        prefix.append(prefix[-1]^nums[i])
    flag=False
    if prefix[-1]==0:
        flag=True
    for i in range(n):
        if flag:
            break
        first=prefix[i]
        for j in range(i+1,n):
            second=prefix[j]^first
            third=prefix[-1]^prefix[j]
            if first==second==third:
                flag=True
                break
    print("YES" if flag else "NO")

t = iinp()
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