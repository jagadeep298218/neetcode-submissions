class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {j: [] for j in range(1,n+1)} 

        for i in range(len(times)):
            source, target, time = times[i]
            adj[source].append([time, target])
        
        minheap = []
        heapq.heappush(minheap, [0, k])
        visited = set()
        res = 0
        while minheap:
            weight, node = heapq.heappop(minheap)
            if node in visited:
                continue
            res = weight
            visited.add(node)
            for new_weight, nei in adj[node]:
                heapq.heappush(minheap, [new_weight+weight, nei])
        if len(visited) == n:
            return res
        return -1
        