class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        transpose=[]
        counter=0
        for i in range(len(strs[0])):
            temp=[]
            for j in range(len(strs)):
                temp.append(strs[j][i])
            transpose.append(temp)
        for i in range(len(transpose)):
            x=sorted(transpose[i])
            if(x!=transpose[i]):
                counter+=1
        return counter