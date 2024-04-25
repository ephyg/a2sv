# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        def isbound(row,col):
            return 0<=row<len(mat) and 0<=col<len(mat[0])

        def neighbours(row,col):
            neigh=[]
            for x,y in directions:
                new_row=x+row
                new_col=y+col
                if isbound(new_row,new_col):
                    neigh.append((new_row,new_col))
            return neigh

        queue=deque()
        for j in range(len(mat)):
            for i in range(len(mat[0])):
                if mat[j][i]==0:
                    queue.append((j,i))

        dp=defaultdict(int)
        visited=set()
        while queue:
            bound=len(queue)
            for i in range(bound):
                row,col=queue.popleft()
                neighbour=neighbours(row,col)
                if mat[row][col]==0:
                    dp[(row,col)]=0
                    for x,y in neighbour:
                        if (x,y) not in visited:
                            queue.append((x,y))
                        visited.add((x,y))
                else: 
                    count=0
                    min_=float("inf")
                    flag=False
                    for x,y in neighbour:
                        if mat[x][y]==0:
                            dp[(row,col)]=1
                            flag=True

                        if (row,col) in dp:
                            min_=min(min_,dp[(row,col)])
                        if (x,y) in dp and not flag:
                            min_=min(min_,dp[(x,y)]+1)
                        if (x,y) not in visited:
                            queue.append((x,y))
                        visited.add((x,y))
                    if min_!=float("inf") and not flag:
                        dp[(row,col)]=min_
        for x,y in dp:
            mat[x][y]=dp[(x,y)]

        return mat
                        

