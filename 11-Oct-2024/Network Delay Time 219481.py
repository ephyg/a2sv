# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        distances = {i:float("inf") for i in range(1,n+1)}
        distances[k]=0
        processed = set()
        heap = [(0,k)]

        while heap:
            curr_distance, curr_node  = heappop(heap)
            if curr_node in processed:
                continue
            processed.add(curr_node)

            for child, weight in graph[curr_node]:
                distance = weight + curr_distance
                if distance < distances[child]:
                    distances[child] = distance
                    heappush(heap,(distance,child))

        if len(processed) != n:
            return -1
        return max(distances.values())