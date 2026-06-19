class Solution:
    def climbStairs(self, n: int) -> int:
        
        def parse(n, cache):
            if n == 1: return 1
            if n == 2: return 2
            if n in cache:
                return cache[n]
            
            cache[n] = parse(n-1, cache) + parse(n-2, cache)
            return cache[n]
        return parse(n, {})