# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(0,len(matrix)-1):
            for j in range(0,len(matrix[0])-1):
                if(matrix[i][j]!=matrix[i+1][j+1]):
                    return False
        return True
                    