# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

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
    operation=n//2+1
    result=[]
    left=1
    right=n*3
    while right > left:
        result.append([left,right])
        left+=3
        right-=3
    print(len(result))
    for x,y in result:
        print(x,y)
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
