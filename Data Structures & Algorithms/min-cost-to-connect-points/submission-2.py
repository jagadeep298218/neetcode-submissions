class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(first, second):
            return abs(first[0] - second[0]) + abs(first[1] - second[1])

        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = manhattan([x1,y1], [x2,y2])
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        minheap = []
        heapq.heappush(minheap, [0, 0])
        visited = set()
        res = 0

        while len(visited) < len(points):
            weight, node = heapq.heappop(minheap)
            if node in visited:
                continue
            res += weight
            visited.add(node)
            for new_weight, nei in adj[node]:
                heapq.heappush(minheap, [new_weight, nei])
        
        return res


        