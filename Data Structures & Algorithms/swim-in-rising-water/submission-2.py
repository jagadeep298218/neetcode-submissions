class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        LEN = len(grid)-1
        minheap = []
        heapq.heappush(minheap, [grid[0][0], 0, 0])
        visited = set()
        res = 0
        while minheap:
            node, row, col = heapq.heappop(minheap)
            if (row, col) in visited:
                continue 
            res = max(res, node)
            visited.add((row, col))
            if row == LEN and col == LEN:
                return res
            if row+1 <= LEN:
                heapq.heappush(minheap, [grid[row+1][col], row+1, col])
            if col + 1 <= LEN:
                heapq.heappush(minheap, [grid[row][col+1], row, col+1])
            if col - 1 >= 0:
                heapq.heappush(minheap, [grid[row][col-1], row, col-1])
            if row - 1 >= 0:
                heapq.heappush(minheap, [grid[row-1][col], row-1, col])
        return -1
        