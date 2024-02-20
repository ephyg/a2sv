class Solution:
    def getRow(self, rowIndex: int ) -> List[int]:
      
        def rec(n):
            if n==0:
                return [1]
            if n==1:
                return [1,1]

            res=rec(n-1)
            row=[1]
            for i in range(len(res)-1):
                row.append(res[i+1]+res[i])
            row.append(1)
            return row
        return rec(rowIndex)