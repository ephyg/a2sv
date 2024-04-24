# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
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


n=iinp()
res=[]
heap=[]
for i in range(n):
    inp=[i for i in input().split()]
    # print(inp)
    cmd,num=1,0
    if len(inp)==2:
        num=int(inp[1])
    cmd=inp[0]
    # print(cmd,num)

    if cmd=="insert":
        heappush(heap,num)
        res.append(f"insert {num}")
    elif cmd=="removeMin":

        if heap:
            res.append("removeMin")
            heappop(heap)
        else:
            heappush(heap,num)
            res.append(f"insert {num}")
            res.append("removeMin")
            heappop(heap)
    else:
        flag=True
        # print(heap)

        while heap :
            if heap[0]<num:
                res.append("removeMin")
                heappop(heap)
            elif heap[0]>num:
                res.append(f"insert {num}")
                heappush(heap,num)
                res.append(f"getMin {num}")
                flag=False
                break
            else:
                res.append(f"getMin {num}")
                flag=False
                break
        if flag:
            res.append(f"insert {num}")
            heappush(heap,num)
            res.append(f"getMin {num}")
            # flag=False
            # break
print(len(res))
for command in res:
    print(command)
            



