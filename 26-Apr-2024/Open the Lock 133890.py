# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbours(wheels):
            temp=wheels[:]
            neigh=[]
            for i in range(4):
                if wheels[i]==0:
                    temp[i]=1
                    neigh.append(temp[:])
                    temp[i]=9
                    neigh.append(temp[:])
                    temp=wheels[:]
                elif wheels[i]==9:
                    temp[i]=1
                    neigh.append(temp[:])
                    temp[i]=8
                    neigh.append(temp[:])
                    temp=wheels[:]
                else:
                    temp[i]-=1
                    neigh.append(temp[:])
                    temp[i]+=2
                    neigh.append(temp[:])
                    temp=wheels[:]
            for i,num in enumerate(neigh):
                neigh[i]=tuple(num)
            return neigh
        queue=deque([((0,0,0,0),0)])
        visited={(0,0,0,0)}
        while queue:
            wheels,cost=queue.popleft()
            strs=[str(i) for i in wheels]
            cast="".join(strs)
            if cast==target:
                return cost
            if cast not in deadends:
                neighbour=neighbours(list(wheels))
                for neigh in neighbour:
                    if neigh not in visited:
                        queue.append((neigh,cost+1))
                        visited.add(neigh)
        return -1



        

