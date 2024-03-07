class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=[row[0] for row in matrix]
        row_index=bisect_left(rows,target)
        if row_index<len(matrix) and rows[row_index]==target:
            return True
        
        col_index=bisect_left(matrix[row_index-1],target)
        if col_index<len(matrix[0]) and matrix[row_index-1][col_index]==target:
            return True
        return False

