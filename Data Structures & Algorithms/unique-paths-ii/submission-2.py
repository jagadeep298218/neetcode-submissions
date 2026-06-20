class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        pairs = {}
        if obstacleGrid[0][0] == 1:
            return 0

        def dp(r, c):
            if c < 0 or r < 0:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == 0 and c == 0:
                return 1 
            if (r, c) in pairs:
                return pairs[(r, c)]
            pairs[(r, c)] = dp(r-1, c) + dp(r, c-1)
            return pairs[(r, c)]

        return dp(len(obstacleGrid)-1, len(obstacleGrid[0])-1)