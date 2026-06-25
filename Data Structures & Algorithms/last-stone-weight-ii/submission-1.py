class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        Stone = sum(stones)
        S = (Stone + 1) // 2
        n = len(stones)

        dp = [[0] * S for _ in range(n + 1)]

        # base case: index == n
        for c in range(S):
            dp[n][c] = abs(Stone - 2 * c)

        # index depends on index+1 -> loop index downward
        for i in range(n - 1, -1, -1):
            for c in range(S):
                skip = dp[i + 1][c]
                nxt = c + stones[i]
                if nxt >= S:                       # curr >= S base case fires
                    take = abs(Stone - 2 * nxt)
                else:
                    take = dp[i + 1][nxt]
                dp[i][c] = min(skip, take)

        return dp[0][0]                            # = knapsack(0, 0)