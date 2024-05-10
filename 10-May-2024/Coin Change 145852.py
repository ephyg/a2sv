# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        
        dp=set()
        queue=deque()
        for i in range(len(coins)):
            queue.append((1,coins[i]))
            dp.add(coins[i])
        while queue:
            bound=len(queue)
            for i in range(bound):
                distance,node=queue.popleft()
                if node==amount:
                    return distance
                for neigh in coins:
                    if (neigh+node)>amount:
                        continue
                    if neigh+node not in dp:
                        queue.append((distance+1,neigh+node))
                        dp.add(neigh+node) 
        return -1
