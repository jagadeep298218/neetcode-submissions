class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weights = {}
        adj = {}
        count = 0
        for i in range(1, n+1):
            weights[i] = float("inf")

        for source, target, weight in times:
            if source not in adj:
                adj[source] = []
            adj[source].append((target, weight))
        
        minheap = []
        heapq.heappush(minheap, (0, k))
        seen = set()

        while minheap:
            weight, source = heapq.heappop(minheap)
            if source in seen:
                continue
            seen.add(source)
            res = weight
            for target, new_weight in adj.get(source, []):
                weights[target] = min(weight+new_weight, weights[target])
                if target not in seen:
                    heapq.heappush(minheap, (weights[target], target))

        if len(seen) == n:
            return res
        else:
            return -1
            