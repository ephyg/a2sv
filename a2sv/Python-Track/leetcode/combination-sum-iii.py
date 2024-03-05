class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans=[]
        def combine(idx,curr,_sum):
            if _sum==n and len(curr)==k:
                ans.append(curr[:])
                return
            if _sum>n:
                return 
            
            for i in range(idx,10):
                curr.append(i)
                _sum+=i
                combine(i+1,curr,_sum)
                _sum-=i
                curr.pop()
            
        combine(1,[],0)
        return ans