# Problem: E - Weighted Cycle Search - https://codeforces.com/gym/520688/problem/E

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


t = iinp()
for _ in range(t):
    n, m = liinp()
    edgesList = []
    for i in range(m):
        edgesList.append(liinp())
    edgesList.sort(key=lambda x: x[2], reverse=True)

    nums = {i: i for i in range(1,n+1)}
    rank = [0]*(n+1)

    def find(x):
        if nums[x] == x:
            return x
        nums[x] = find(nums[x])
        return nums[x]
    min_ = float("inf")
    min_edge = []

    def union(x, y, weight):
        global min_edge,min_
        xx = find(nums[x])
        yy = find(nums[y])
        if xx != yy:
            if rank[yy] < rank[xx]:
                nums[yy] = xx
            elif rank[xx] < rank[yy]:
                nums[xx] = yy
            else:
                rank[xx] += 1
                nums[yy] = xx
        else:
            if min_ > weight:
                min_ = min(min_, weight)
                min_edge = [x, y]
    graph=defaultdict(list)
    for x, y, weight in edgesList:
        if find(x)!=find(y):
            graph[x].append(y)
            graph[y].append(x)
        union(x, y, weight)
    
        
    # print(graph)
    queue=deque([min_edge[0]])
    visited={min_edge[0]}
    ans=[]
    shortestPath={min_edge[0]:False}
    while queue:
        bound=len(queue)
        for i in range(bound):
            node=queue.popleft()
            if node==min_edge[1]:
                # queue.clear
                break
            for neighbour in graph[node]:
                if neighbour not in visited:
                    shortestPath[neighbour]=node
                    queue.append(neighbour)
                    visited.add(neighbour)
    end=min_edge[1]
    ans.append(min_edge[0])
    while shortestPath[end]:
        ans.append(end)
        end=shortestPath[end]
        
    print(min_,len(ans))
    print(*ans)
