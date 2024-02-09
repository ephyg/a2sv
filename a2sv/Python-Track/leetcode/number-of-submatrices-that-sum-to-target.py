class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row=len(matrix)
        col=len(matrix[0])
        prefix=[[0]*(col+1) for i in range(row+1)]
        for r in range(1,row+1):
            for c in range(1,col+1):
                prefix[r][c]=prefix[r][c-1]+prefix[r-1][c]-prefix[r-1][c-1]+matrix[r-1][c-1]
        print(prefix)
        count=0
        for r1 in range(1,row+1):
            for r2 in range(r1,row+1):
                frequency=defaultdict(int)
                frequency[0]=1
                for c in range(1,col+1):
                    currSum=prefix[r2][c]-prefix[r1-1][c]
                    count+=frequency[currSum-target]
                    frequency[currSum]+=1
        return count

                
        
            


        return 2