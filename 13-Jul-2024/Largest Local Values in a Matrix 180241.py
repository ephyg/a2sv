# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        matrix = []
        temp = []

        for r in range(len(grid) - 2):
            temp = []
            for c in range(len(grid) - 2):
                mx = 0
                for i in range(3):
                    for j in range(3):
                        mx = max(grid[i + r][j + c], mx)

                temp.append(mx)
            matrix.append(temp)
        return matrix
