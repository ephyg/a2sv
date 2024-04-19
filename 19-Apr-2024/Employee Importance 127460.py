# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # print(employees[0].importance)
        graph=defaultdict(list)
        important=defaultdict(int)
        for i in range(len(employees)):
            graph[employees[i].id].extend(employees[i].subordinates)
            important[employees[i].id]=employees[i].importance



        queue=deque([id])

        result=0
        while queue:
            bound=len(queue)
            for i in range(bound):
                node=queue.popleft()
                result+=important[node]
                for neighbour in graph[node]:   
                    queue.append(neighbour)
        
        return result