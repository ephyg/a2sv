# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        idx=defaultdict(tuple)
        for i in range(len(queries)):
            idx[i]=tuple(queries[i])
        queries.sort(key=lambda x:x[2])
        edgeList.sort(key=lambda x:x[2])
        
        nums={i:i for i in range(n)}
        rank=defaultdict(int)
        def find(x):
            if nums[x]==x:
                return x
            nums[x]=find(nums[x])
            return nums[x]

        def unions(x,y):
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
        ans=defaultdict(bool)


        left = 0
        for right in range(len(queries)):
            while left<len(edgeList) and queries[right][2]>edgeList[left][2]:
                
                x = find(nums[edgeList[left][0]])
                y = find(nums[edgeList[left][1]])
                if x!=y:
                    unions(x,y)
                left+=1

            xx = find(nums[queries[right][0]])
            yy = find(nums[queries[right][1]])
            if xx==yy:
                ans[tuple(queries[right])]=True

        res=[]
        for i in range(len(queries)):
            res.append(ans[idx[i]])
        return res