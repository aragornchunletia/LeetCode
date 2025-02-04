class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1) ,len(word2)
        if 0 in (m,n):
            return 0 if m==n else 1

        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        for i in range(1,(n+1)):
            for j in range(1,(m+1)):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],
                                       dp[i][j-1],
                                       dp[i-1][j])

        return dp[n][m]



        """
        def recur(i ,j):
            if i == n:
                return m-j
            if j == m:
                return n-i
            if memo[i][j] != -1:
                return memo[i][j]
            if word1[i] == word2[j]:
                memo[i][j] = recur(i+1 , j+1)
                return memo[i][j]
            replace = 1 + recur(i+1 , j+1)
            remove = 1 + recur(i+1 ,j)
            add = 1 + recur(i,j+1)
            memo[i][j] = min(replace , remove , add)
            return memo[i][j]

        return recur(0,0)
"""
        