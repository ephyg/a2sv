class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        transpose=list(zip(*grid))
        tot=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                tot+=(min(max(transpose[c]),max(grid[r])))-grid[r][c]
        return tot