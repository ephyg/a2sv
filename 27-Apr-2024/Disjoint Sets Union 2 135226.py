# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

from collections import defaultdict
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


n,m=liinp()
nums={i:i for i in range(n+1)}
rank=defaultdict(int)
size=[1]*(n+1)
max_=[i for i in range(n+1)]
min_=[i for i in range(n+1)]

def find(x):
    if nums[x]==x:
        return x
    nums[x]=find(nums[x])
    return nums[x]


def union(x,y):
    xx=find(nums[x])
    yy=find(nums[y])
    if xx!=yy :
        if rank[yy] < rank[xx]:
            nums[yy] = xx
            max_[xx]=max(max_[yy],max_[xx])
            min_[xx]=min(min_[yy],min_[xx])
            size[xx]+=size[yy]
        elif rank[xx] < rank[yy]:
            nums[xx] = yy
            max_[yy]=max(max_[xx],max_[yy])
            min_[yy]=min(min_[xx],min_[yy])
            size[yy]+=size[xx]
        else:
            rank[xx]+=1
            nums[yy]=xx
            max_[xx]=max(max_[yy],max_[xx])
            min_[xx]=min(min_[yy],min_[xx])
            size[xx]+=size[yy]
for i in range(m):
    cmd=lsinp()
    if cmd[0]=="union":
        union(int(cmd[1]),int(cmd[2]))
    else:
        parent=find(int(cmd[1]))
        print(min_[int(parent)],max_[int(parent)],size[int(parent)])




