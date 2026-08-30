class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        def dfs(x, y):
            if (x < 0) or (x >= ROWS) or (y < 0) or (y >= COLS):
                return 1
            if grid[x][y] == 0:
                return 1
            if(x, y) not in seen:
                seen.add((x, y))
                return dfs(x+1, y) + dfs(x, y+1) + dfs(x-1, y) + dfs(x, y-1)
            else:
                return 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i, j)

        