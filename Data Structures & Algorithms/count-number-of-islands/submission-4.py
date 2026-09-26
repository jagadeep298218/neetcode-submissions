class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        seen = set()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        def dfs(r, c):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS):
                return 
            seen.add((r, c))
            if grid[r][c] == "0":
                return 
            else:
                grid[r][c] = "0"
            for dx, dy in dirs:
                dfs(r+dx, c+dy)


        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == "1"):
                    res += 1
                    dfs(r, c)
        return res