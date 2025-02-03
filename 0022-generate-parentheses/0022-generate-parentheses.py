class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = ""
        res = []

        def backtrack(open , close):
            nonlocal stack
            if open == close == n:
                res.append(stack[:])
                return

            if open < n:
                stack += '('
                backtrack(open + 1 , close)
                stack = stack[:-1]

            if close < open:
                stack += ')'
                backtrack(open , close + 1)
                stack = stack[:-1]

            return

        backtrack(0,0)
        return res