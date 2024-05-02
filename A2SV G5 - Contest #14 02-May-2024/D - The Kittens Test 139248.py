# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D

from collections import Counter, defaultdict, deque
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


n = iinp()
nums = {i: i for i in range(1,n+1)}
rank = [0]*(n+1)    

def find(x):
    if nums[x] == x:
        return x
    nums[x] = find(nums[x])
    return nums[x]
answer={i:[i] for i in range(1,n+1)}
def union(x, y):
    global answer
    xx = find(nums[x])
    yy = find(nums[y])
    if xx != yy:
        if rank[yy] < rank[xx]:
            nums[yy] = xx
            answer[xx].extend(answer[yy])
            answer.pop(yy)
        elif rank[xx] < rank[yy]:
            nums[xx] = yy
            answer[yy].extend(answer[xx])
            answer.pop(xx)
        else:
            rank[xx] += 1
            nums[yy] = xx
            answer[xx].extend(answer[yy])
            answer.pop(yy)
        
for _ in range(n-1):
    a,b = liinp()
    union(a,b)
res=[]
for num in answer:
    res.extend(answer[num])
print(*res)