class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        Stone = sum(stones)
        S = (Stone+1) // 2
        memo = {}

        def knapsack(curr, index):
            if curr >= S or index >= len(stones):
                return abs(Stone - 2*curr)
            if (curr, index) in memo:
                return memo[(curr, index)]
            memo[(curr, index)] = min(knapsack(curr, index+1), knapsack(curr+stones[index], index+1))
            return memo[(curr, index)]

        return knapsack(0,0)
