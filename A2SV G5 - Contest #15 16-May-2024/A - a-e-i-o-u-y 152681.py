# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

import sys
from collections import defaultdict,Counter,deque
from math import ceil,gcd
n=int(sys.stdin.readline().strip())
s=sys.stdin.readline().strip()
vowels="aeiouy"
stack=[]
for i in range(n):
    if not stack:
        stack.append(s[i])
    else:
        if stack[-1] in vowels and s[i] in vowels:
            continue
        else:
            stack.append(s[i])
print("".join(stack))
        
