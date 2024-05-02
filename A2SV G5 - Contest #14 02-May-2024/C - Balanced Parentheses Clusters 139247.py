# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

from collections import Counter, defaultdict
from math import ceil
import sys
def lsinp():
    return sys.stdin.readline().strip().split()
def liinp():
    return list(map(int, sys.stdin.readline().strip().split()))
def sinp():
    return sys.stdin.readline().strip()
def iinp():
    return int(sys.stdin.readline().strip())
 

t=iinp()
for i in range(t):
    n=iinp()
    s=sinp()

    for i in range(1,len(s)):
        if s[i-1]==")" and s[i]=="(":
            n-=1
    print(n)