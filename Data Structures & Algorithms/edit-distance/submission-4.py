class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

        for i in range(len(word2)+1):
            dp[0][i] = i
        for j in range(len(word1)+1):
            dp[j][0] = j
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                val = min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1])
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else: 
                    dp[i][j] = val+1
        return dp[-1][-1]


        memo = {}
        def dp(i1, i2):
            if i1 == len(word1):
                return len(word2) - i2
            if i2 == len(word2):
                return len(word1) - i1    
            if word1[i1] == word2[i2]:
                return dp(i1+1, i2+1)
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            memo[(i1, i2)] = 1 + min(min(dp(i1+1, i2+1), dp(i1+1, i2)), dp(i1, i2+1))
            return memo[(i1, i2)]
        return dp(0, 0)
