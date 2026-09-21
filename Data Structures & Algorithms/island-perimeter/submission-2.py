class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        seen = set()
        def dfs(row, col):
            if (row < 0) or (row >= ROWS) or (col < 0) or (col >= COLS):
                return 1
            if (row, col) in seen:
                return 0
            if grid[row][col] == 0:
                return 1
            else:
                seen.add((row, col))
            return dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==1:
                    res += dfs(r, c)
        
        return res
        

        