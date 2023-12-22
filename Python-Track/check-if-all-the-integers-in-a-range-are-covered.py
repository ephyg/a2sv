class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        counter=0
        for i in range(left,right+1):
            for j in range(len(ranges)):
                if(ranges[j][0]<=i and ranges[j][1]>=i):
                    counter+=1
                    break
        if(counter==(right-left+1)):
            return True
        else:
            return False
            