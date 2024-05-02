# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

import sys
from collections import defaultdict,Counter,deque
from math import ceil,gcd
n,m,k=list(map(int, sys.stdin.readline().strip().split()))
nums=[]
for i in range(m+1):
    num=int(sys.stdin.readline().strip())
    nums.append(num)
    # print(bin(num)[2:])
ans=0
last=nums[-1]
for i in range(m):
    count=0
    temp=last
    while temp | nums[i]:
        if temp%2!=nums[i]%2:
            count+=1
        temp>>=1
        nums[i]>>=1
    if count<=k:
        ans+=1
print(ans)




