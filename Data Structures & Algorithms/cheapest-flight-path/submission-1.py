class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for source, dest, cost in flights:
            adj[source].append([cost, dest])
        
        minheap = []
        heapq.heappush(minheap, [0, src, 0])
        visited = {i:float("inf") for i in range(n)}

        while minheap:
            cost, source, steps = heapq.heappop(minheap)
            if source == dst:
                return cost
            if visited[source] <= steps:
                continue
            visited[source] = steps
            for new_cost, nei in adj[source]:
                if steps <= k:
                    heapq.heappush(minheap, [new_cost+cost, nei, steps+1])

        return -1



            