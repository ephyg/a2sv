class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dict=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in dict:
                    dict[i+j].append(mat[i][j])
                else:
                    dict[i+j]=[mat[i][j]]
        answer=[]
        for key , value in dict.items():
            if key%2==0:
                answer.extend(value[::-1])
            else:
                answer.extend(value)
        return answer

