class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            if (x >= ROWS or x < 0) or (y >= COLS or y < 0):
                return 
            if grid[x][y] == "0":
                return 
            grid[x][y] = "0"
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "0":
                    dfs(r, c)
                    res += 1
        return res
