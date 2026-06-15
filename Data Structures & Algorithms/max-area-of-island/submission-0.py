class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        seen = []
        ones = 0
        m = 0
        def dfs(r, c):
            nonlocal ones
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            if r < 0 or r >= rows or c < 0 or c >= columns:
                return 
            if [r, c] in seen or grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                seen.append([r, c])
                ones += 1
                
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for r in range(rows):
            for c in range(columns):
                ones = 0
                dfs(r, c)
                if ones > m:
                    m = ones
        return m
            