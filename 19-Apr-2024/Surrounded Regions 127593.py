# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def isbound(row,col):
            return 0<=row<len(board) and 0<=col<len(board[0])
        def neighbours(row,col):
            neigh=[]
            for x,y in directions:
                new_row=row+x
                new_col=col+y
                if isbound(new_row,new_col):
                    if board[new_row][new_col]=="O":
                        neigh.append((new_row,new_col))
                else:
                    return (False,[])
            return (True,neigh)

        temp=[]
        def bfs(row,col):
            visited=set()
            nonlocal temp
            queue=deque()
            queue.append((row,col))
            visited.add((r,c))

            while queue:
                bound=len(queue)
                for i in range(bound):
                    row,col=queue.popleft()
                    flag,neighbour=neighbours(row,col)
                    temp.append((row,col))

                    if flag:
                        for x,y in neighbour:
                            if (x,y) not in visited:
                                queue.append((x,y))
                                visited.add((x,y))
                    else:
                        temp=[]
                        return False
            return True
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O":
                    if bfs(r,c):
                        for x,y in temp:
                            board[x][y]="X"
                    temp=[]
        return board

                        