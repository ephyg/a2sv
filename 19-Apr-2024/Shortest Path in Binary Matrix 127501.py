# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        def isbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        def neighbours(row,col):
            neigh=[]
            for x,y in directions:
                new_row=row+x
                new_col=col+y
                if isbound(new_row,new_col) and grid[new_row][new_col]==0:
                    neigh.append((new_row,new_col))
            return neigh
        if grid[0][0]:
            return -1
        queue=deque([(0,0,1)])
        while queue:
            bound=len(queue)
            for i in range(bound):
                row,col,nodeNumber=queue.popleft()
                if (row,col)==(len(grid)-1,len(grid[0])-1):
                        return nodeNumber
                        
                neighbour=neighbours(row,col)
                for x,y in neighbour:
                    grid[x][y]=1
                    queue.append((x,y,nodeNumber+1))
                    
        return -1

