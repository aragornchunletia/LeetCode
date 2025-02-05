class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(start , end):
            while start <= end:
                if s[start] != s[end]:  return False
                start , end = start+1 ,end-1
            return True


        def helper(sIdx , part):
            if sIdx == N:
                res.append(part[:])
                return
            #backtrac through all lengths of substrs
            for i in range(sIdx , N):
                if isPalindrome(sIdx , i):
                    part.append(s[sIdx:i+1])
                    helper(i+1 , part)
                    part.pop()


        N = len(s)
        res = []
        helper(0,[])
        return res


