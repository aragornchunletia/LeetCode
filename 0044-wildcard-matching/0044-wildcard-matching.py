
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[-1]*len(p) for _ in range(len(s))]

        def helper(idxS , idxP):
            if idxS < 0 and idxP < 0:
                return True

            if idxS >= 0 and idxP < 0:
                return False

            if idxS < 0 and idxP >=0:
                for i in range(idxP+1):
                    if p[i] != "*":  return False
                return True

            if dp[idxS][idxP] != -1:    return dp[idxS][idxP]
            # if positional characters are equal or "?" char we move ahead
            if s[idxS] == p[idxP] or p[idxP] == "?":
                dp[idxS][idxP] =  helper(idxS-1 , idxP-1)
                return dp[idxS][idxP]
            # if positional char is a wildcard, we either use it and move ahead
            # or we do not use it and move ahead
            if p[idxP] == "*":
                dp[idxS][idxP] = helper(idxS-1 , idxP) or helper(idxS , idxP-1)
                return dp[idxS][idxP]

            dp[idxS][idxP] = False

            return dp[idxS][idxP]

        return helper(len(s)-1 , len(p)-1)
        