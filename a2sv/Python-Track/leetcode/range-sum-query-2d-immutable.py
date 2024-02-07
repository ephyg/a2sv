class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefixSum=[]
        

        for i in range(len(matrix)+1):
            self.prefixSum.append([0]*(len(matrix[0])+1))
        self.r=len(self.prefixSum)
        self.c=len(self.prefixSum[0])
        for r in range(1,self.r):
            for c in range(1,self.c):
                self.prefixSum[r][c]+=(self.prefixSum[r-1][c]+self.prefixSum[r][c-1]-self.prefixSum[r-1][c-1]+matrix[r-1][c-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.prefixSum[row2+1][col2+1]-self.prefixSum[row2+1][col1]-self.prefixSum[row1][col2+1]+self.prefixSum[row1][col1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)