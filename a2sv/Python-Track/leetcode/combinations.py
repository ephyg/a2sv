class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans=[]
        def combination (idx,temp):
            if len(temp)==k:
                ans.append(temp[:])
                return 
            for i in range(idx,n+1):
                temp.append(i)
                combination(i+1,temp)
                temp.pop()
        combination(1,[])
        return ans
