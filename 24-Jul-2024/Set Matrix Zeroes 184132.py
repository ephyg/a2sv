# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    for i in range(len(matrix)):
                        if matrix[i][c]:
                            matrix[i][c]=""
                    for j in range(len(matrix[0])):
                        if matrix[r][j]:
                            matrix[r][j]=""
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]=="":
                    matrix[r][c]=0

