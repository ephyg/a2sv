# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys
from collections import defaultdict,Counter,deque
from math import ceil,gcd
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    length=n.bit_length()
    binary=bin(n)[2:]
    count=binary.count("1")
    if n==1:
        print(3)
    elif count==1:
        print(2**(length-1)+1)
    else:
        for i,num in enumerate(binary[::-1]):
            if num=="1":
                print(2**i)
                break




