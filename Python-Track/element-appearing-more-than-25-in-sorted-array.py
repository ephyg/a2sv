class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x=list(set(arr))
        for i in range(len(x)):
            y=arr.count(x[i])
            calc=(y/len(arr))*100
            if(calc>25):
                return x[i]
            