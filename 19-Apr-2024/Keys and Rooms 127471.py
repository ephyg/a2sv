# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        count=0
        queue=deque([0])
        visited={0}
        while queue:
            bound=len(queue)
            for i in range(bound):
                node=queue.popleft()
                for neighbour in rooms[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        count+=1
                    visited.add(neighbour)
        return count+1==len(rooms)