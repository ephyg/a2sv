# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n = len(board)
        def to_row_col(cell):
            r = (cell-1)//n
            c = (cell-1)%n 
            if r%2!=0:
                c = n-1-c
            return (r,c)

        queue = deque([(1,0)])
        visited = set()


        while queue:
            cell,dist = queue.popleft()
            for i in range(1,7):
                new_cell = cell+i
                r,c = to_row_col(new_cell)
                if board[r][c] != -1:
                    new_cell = board[r][c]
                if new_cell == n*n:
                    return dist+1
                if (r,c) not in visited:
                    queue.append((new_cell,dist+1))
                    visited.add((r,c))
        return -1
