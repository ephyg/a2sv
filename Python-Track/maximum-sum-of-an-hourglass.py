class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        _row=len(grid)-2
        _column=len(grid[0])-2
        total=0
        for i in range(_row):
            for j in range(_column):
                row1=sum(grid[i][j:j+3])
                center=grid[i+1][j+1]
                row3=sum(grid[i+2][j:j+3])
                res=row1+center+row3
                total=max(res,total)
        return total