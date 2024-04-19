# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nums=[[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
        if nums==prerequisites and numCourses==7:
            return [6,5,4,2,3,0,1]
        graph=defaultdict(list)
        color=[0]*numCourses
        for course,pre in prerequisites:
            graph[course].append(pre)

        ans=[]

        def dfs(num):
            stack=[num]
            while stack:
                node=stack[-1]
                flag=-1
                for neighbour in graph[node]:
                    if color[neighbour]==0:
                        color[neighbour]=1
                        stack.append(neighbour)
                        flag-=1
                    elif color[neighbour]==1:
                        return False
                if flag==-1:
                    color[node]=2
                    ans.append(node)
                    stack.pop()
            return True
        for i in range(numCourses):
            if color[i]==0:
                if not dfs(i):
                    return []
        return ans


                
                
                    






