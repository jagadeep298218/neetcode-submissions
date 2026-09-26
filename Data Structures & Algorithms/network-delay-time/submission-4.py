class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Djikstras algorithm
        '''
        edges = defaultdict(list)

        for src, target, dist in times:
            edges[src].append([target, dist])

        minheap = []
        seen = set()
        heapq.heappush(minheap, (0, k))

        while minheap:
            dist, src = heapq.heappop(minheap)
            if src in seen:
                continue
            seen.add(src)

            if len(seen) == n:
                return dist
            for target, dist2 in edges[src]:
                if target not in seen:
                    heapq.heappush(minheap, (dist+dist2, target))
        return -1


