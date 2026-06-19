class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for i in range(n)] for j in range(m)]

        def recursion(r, c):
            nonlocal cache
            if r == 0 or c == 0:
                cache[r][c] = 1
                return 1
            if cache[r][c] > 0:
                return cache[r][c]
            cache[r][c] = recursion(r-1, c) + recursion(r, c-1)
            return cache[r][c]
        
        return recursion(m-1, n-1)
