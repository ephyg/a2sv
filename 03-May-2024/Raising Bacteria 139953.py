# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

import sys
from collections import defaultdict,Counter,deque
from math import ceil,gcd
n=int(sys.stdin.readline().strip())

count=n.bit_length()
print(bin(n)[2:].count("1"))