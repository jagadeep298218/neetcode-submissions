class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]    
        
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else: 
                    dp[i][j] += max(dp[i-1][j], dp[i][j-1])
        
        return dp[len(text1)][len(text2)]

        memo = {}
        def dfs(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0 
            if text1[i1] == text2[i2]:
                return 1 + dfs(i1+1, i2+1)
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            memo[(i1, i2)] = max(dfs(i1+1, i2), dfs(i1, i2+1))  
            return memo[(i1, i2)]      

        return dfs(0, 0)
