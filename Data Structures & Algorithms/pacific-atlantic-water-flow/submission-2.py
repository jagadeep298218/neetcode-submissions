class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows = len(heights)
        cols = len(heights[0])

        pacific, atlantic = set(), set()

        res = []

        def dfs(row, col, visited):
            visited.add((row, col))

            direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for r, c in direction:
                r, c = row + r, col + c

                if (0 <= r < rows and 0 <= c < cols and (r, c) not in visited and heights[r][c] >= heights[row][col]):
                    dfs(r, c, visited)


        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols -1, atlantic)


        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])


        return res