# Problem: Anji's Binary Tree - https://codeforces.com/contest/1900/problem/C

from collections import defaultdict, deque
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

for _ in range(iinp()):
    n=iinp()
    s=sinp()
    graph=defaultdict(list)
    direction=defaultdict(str)
    for i in range(n):
        nums=[i for i in liinp()]
        graph[i+1].extend(nums)
        direction[i+1]=s[i]
    
    
    queue=deque()
    queue.append((1,0))
    min_=float("inf")
      
    while queue:
        bound=len(queue)
        for i in range(bound):
            node,operation=queue.popleft()
            left=graph[node][0]
            right=graph[node][1]
            if left==0 and right==0:
                min_=min(operation,min_)
            if left:
                if direction[node]=="L":
                    queue.append((left,operation))
                else:
                    queue.append((left,operation+1))
            if right:
                if direction[node]=="R":
                    queue.append((right,operation))
                else:
                    queue.append((right,operation+1))     
    print(min_)






