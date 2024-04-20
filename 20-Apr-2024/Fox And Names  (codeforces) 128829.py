# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque

names=[]
graph=defaultdict(list)
n=int(input())
for _ in range(n):
    s=input()
    names.append(s)
degree=defaultdict(int)
flag=True
for i in range(1,n):
    if names[i][0]!=names[i-1][0]:
        graph[names[i-1][0]].append(names[i][0])
        degree[names[i][0]]+=1
    else:
        pointer=0
        while len(names[i])>pointer and len(names[i-1])>pointer:
            if names[i][pointer]==names[i-1][pointer]:
                if pointer==len(names[i])-1 and len(names[i]) < len(names[i-1]) :
                    flag=False
                    break
            else:
                graph[names[i-1][pointer]].append(names[i][pointer])
                degree[names[i][pointer]]+=1
                break
            pointer+=1
            
                
            

queue=deque()
for i in range(ord("a"),ord("z")+1):
    if degree[chr(i)]==0:
        queue.append(chr(i))
ans=[]
while queue:
    node=queue.popleft()
    ans.append(node)
    for neighbour in graph[node]:
        degree[neighbour]-=1
        if degree[neighbour]==0:
            queue.append(neighbour)
if len(ans)!=26 or not flag:
    print("Impossible")
else:
    print("".join(ans))
# print(queue)