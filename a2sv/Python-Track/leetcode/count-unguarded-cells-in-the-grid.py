class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        guard=set(tuple(i) for i in guards)
        wall=set(tuple(i) for i in walls)

        visited=set()
        for (x,y) in guard:
            # visit right
            x_r=x+1
            while x_r < m and (x_r,y) not in guard and (x_r,y) not in wall:
                visited.add((x_r,y))
                x_r+=1
            # visit left
            x_l=x-1
            while x_l > -1 and (x_l,y) not in guard and (x_l,y) not in wall:
                visited.add((x_l,y))
                x_l-=1
            # visit down
            y_d=y+1
            while y_d<n and (x,y_d) not in guard and (x,y_d) not in wall:
                visited.add((x,y_d))
                y_d+=1
            # visit up
            y_u=y-1
            while y_u>-1 and (x,y_u) not in guard and (x,y_u) not in wall:
                visited.add((x,y_u))
                y_u-=1
        print(visited)
        # print(guard,wall)
        return (n*m)-len(guards)-len(walls)-len(visited)

        
