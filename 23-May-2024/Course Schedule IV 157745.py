# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(set)
        indegree=[0]*numCourses
        for a,b in prerequisites:
            graph[b].add(a)
            indegree[a]+=1
        
        result=defaultdict(set)
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            node=queue.popleft()
            for neigh in graph[node]:
                result[neigh].add(node)
                for num in result[node]:
                    result[neigh].add(num)
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        ans=[]
        for a,b in queries:
            if a in result and b in result[a]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


        