class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # i, j represent the used length in s1 and s2

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if not dp[j]:
                    continue
                # if s1[i] == s3[i+j]:
                if i < len(s1):
                    dp[j] = s1[i] == s3[i+j]

                if j < len(s2) and s2[j] == s3[i+j]:
                    dp[j+1] = True
        
        return dp[-1]


        