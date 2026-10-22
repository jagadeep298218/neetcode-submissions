class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''fewest number of coins
        function: return min number coins. states: curr_amount, 
        base: if curr > amount: return inf
              if curr == amount: return 0
        recursion: 
            best = inf
            for i in coins:
                best = min(i + dp(i+curr_amount), best)
            return best'''

        def dp(curr):
            if curr > amount:
                return float("inf")
            if curr == amount:
                return 0
            if curr in cache:
                return cache[curr]
            best = float("inf")
            for i in coins:
                best = min(1 + dp(i+curr), best)
            cache[curr] = best
            return cache[curr]
        cache = {}
        res = dp(0)
        return -1 if res == float("inf") else res
