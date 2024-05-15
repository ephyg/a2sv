# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

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
    
    
    
def solve(n,k,nums):
    suffix=[0]*(n)
    for i in range(n-1,-1,-1):
        if i==n-1:
            suffix[i]=nums[i]
            continue
        suffix[i]=suffix[i+1]+nums[i]
    ans=suffix[0]
    suffix=sorted(suffix[1:])
    ans+=sum(suffix[len(suffix)-k+1:])
    print(ans)
    
    return

# t = iinp()
# for _ in range(t):
n,k=liinp()
nums=liinp()
solve(n,k,nums)


# def main():
#     pass

# if __name__ == '__main__':

#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()