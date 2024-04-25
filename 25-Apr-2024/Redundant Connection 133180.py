# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        nums={i:i for i in range(1,len(edges)+1)}
        rank=defaultdict(int)

        def find(x):
            if nums[x]==x:
                return x
            nums[x]=find(nums[x])
            return nums[x]
        ans=[]
        def union(x,y):
            xx=find(nums[x])
            yy=find(nums[y])
            if xx!=yy :
                if rank[yy] < rank[xx]:
                    nums[yy] = xx
                elif rank[xx] < rank[yy]:
                    nums[xx] = yy
                else:
                    rank[xx]+=1
                    nums[yy]=xx
            else:
                ans.append([x,y]) 
        for x,y in edges:
            union(x,y)
        
        if ans:
            return ans[-1]
        return []



        