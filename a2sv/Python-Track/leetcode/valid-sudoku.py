class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transpose=list(zip(*board))
        for i in range(9):
            for j in range(9):
                if board[i][j] !=".":
                    if board[i][j] in board[i][:j] or board[i][j] in board[i][j+1:]:
                        return False
                    if board[i][j] in transpose[j][:i] or board[i][j] in transpose[j][i+1:]:
                        return False
        check=[True]*9
        for r in range(0,9,3):
            for c in range(0,9,3):
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j]==".":
                            continue
                        elif check[int(board[i][j])-1]:
                            check[int(board[i][j])-1]=False
                        else:
                            return False
                check=[True]*9
        return True
        

        