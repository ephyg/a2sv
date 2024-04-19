# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        def neighbours(row,col):
            neigh=[]
            for x,y in directions:
                new_row=row+x
                new_col=col+y
                if isbound(new_row,new_col) and grid[new_row][new_col]==1:
                    neigh.append((new_row,new_col))
            return neigh

        queue=deque()
        fresh=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        ans=0
        while queue:
            if fresh==0:
                return ans
            bound=len(queue)
            for i in range(bound):
                row,col=queue.popleft()
                neighbour=neighbours(row,col)

                for x,y in neighbour:
                    grid[x][y]=2
                    queue.append((x,y))
                    fresh-=1
            ans+=1

        if fresh==0:
            return ans
        return -1
        
            


                    



        