# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

import sys
from collections import defaultdict, Counter, deque
from math import ceil, gcd
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    bits = [0]*35
    for i in range(n):
        temp = bin(nums[i])[2:]
        x = 35-len(temp)
        temp = "0"*x+temp
        for i in range(35):
            if temp[i] == "0":
                bits[i] += 1        
    ans = 0
    for i in range(4,35):
        if bits[i] <= k:
            ans += pow(2, 34-i)
            k -= bits[i]
    print(ans)
