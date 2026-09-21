class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set()
        def dfs(row, col):
            if (row < 0) or (col < 0) or (row >= ROWS) or (col >= COLS):
                return 
            if grid[row][col] == "0" or (row, col) in seen:
                return 
            else:
                seen.add((row, col))
            return dfs(row+1, col), dfs(row-1, col), dfs(row, col+1), dfs(row, col-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and ((r, c) not in seen):
                    res += 1
                    dfs(r, c)
        return res