# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        n=len(matrix)
        m=len(matrix[0])

        def isbound(row,col):
            return 0<=row<n and 0<=col<m

        graph=defaultdict(list)
        indegree = [[0]*m for i in range(n)]
        for r in range(n):
            for c in range(m):
                for x,y in directions:
                    new_r=x+r
                    new_c=y+c
                    if isbound(new_r,new_c) and matrix[r][c]>matrix[new_r][new_c]:
                        graph[(r,c)].append((new_r,new_c))
                        indegree[new_r][new_c]+=1
        
        queue=deque()
        for r in range(n):
            for c in range(m):
                if indegree[r][c]==0:
                    queue.append((r,c,1))
        ans=0
        while queue:
            bound=len(queue)
            for i in range(bound):
                row,col,dist=queue.popleft()
                ans=max(ans,dist)
                for x,y in graph[(row,col)]:
                    indegree[x][y]-=1
                    if indegree[x][y]==0:
                        queue.append((x,y,dist+1))
                
        return ans

        # directions=[(-1,0),(0,-1),(1,0),(0,1)]
        # n=len(matrix)
        # m=len(matrix[0])

        # def isbound(row,col):
        #     return 0<=row<n and 0<=col<m
        # memo={}
        # def dp(row,col):
        #     if (row,col) not in memo:
        #         answer=1
        #         for x,y in directions:
        #             new_r=x+row
        #             new_c=y+col
        #             if isbound(new_r,new_c) and matrix[row][col]>matrix[new_r][new_c]:
        #                 answer=max(answer,dp(new_r,new_c)+1)
        #         memo[(row,col)]=answer
        #     return memo[(row,col)]

        # res=0
        # for r in range(n):
        #     for c in range(m):
        #         res=max(dp(r,c),res)
        # return res


# tried with bottom - up
        # n=len(matrix)
        # m=len(matrix[0])

        # increasing=[[0]*(len(matrix[0])) for i in range(len(matrix))]
        # decreasing=[[0]*(len(matrix[0])) for i in range(len(matrix))]

        # directions=[(-1,0),(0,-1)]
        # def isbound(row,col):
        #     return 0<=row<n and 0<=col<m

        # for r in range(n):
        #     for c in range(m):
        #         max_=1
        #         for x,y in directions:
        #             new_r=x+r
        #             new_c=y+c
        #             if isbound(new_r,new_c):
        #                 if matrix[r][c] > matrix[new_r][new_c]:
        #                     max_=max(max_,increasing[new_r][new_c]+1)
        #         increasing[r][c]=max_
        # for r in range(n):
        #     for c in range(m):
        #         max_=1
        #         for x,y in directions:
        #             new_r=x+r
        #             new_c=y+c
        #             if isbound(new_r,new_c):
        #                 if matrix[r][c] < matrix[new_r][new_c]:
        #                     max_=max(max_,decreasing[new_r][new_c]+1)
        #         decreasing[r][c]=max_

        # def findMax(grid):
        #     mx=0
        #     for r in range(n):
        #         for c in range(m):
        #             mx=max(mx,grid[r][c])
        #     return mx
        
        # dec=findMax(decreasing)
        # inc=findMax(increasing)
        # return max(dec,inc)

        return 3
        
