# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        answer=[]
        count=0
        if len(original)!=(m*n):
            return []
        for r in range(m):
            temp=[]
            for c in range(n):
                temp.append(original[count])
                count+=1
            answer.append(temp)
        return [] if count!=len(original) else answer