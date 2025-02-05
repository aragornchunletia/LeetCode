class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True #empty string

        for i in range(1 , n+1):
            for j in range(i):
                substr = s[j:i]
                if substr in wordDict and dp[j]:
                    dp[i] = True
                    break

        return dp[n]
