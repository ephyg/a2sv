# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

import sys
from collections import defaultdict,Counter,deque
from math import ceil,gcd
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,z=list(map(int, sys.stdin.readline().strip().split()))
    nums=list(map(int, sys.stdin.readline().strip().split()))
    max_=float("-inf")
    for i in range(n):
        And=z&nums[i]
        z=max(And,z)
    for j in range(n):
        otherOr=z|nums[j]
        otherAnd=z|nums[j]
        max_=max(otherOr,otherAnd,max_)
    print(max_)

