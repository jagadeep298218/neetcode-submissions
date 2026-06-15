class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        seen = set()
        res = 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= columns:
                return 0
            if (r, c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r, c))
                   
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
    
        for r in range(rows):
            for c in range(columns):
                res = max(dfs(r, c), res)
        return res
            