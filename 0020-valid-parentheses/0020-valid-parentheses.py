from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        openning = ['(' ,'{' ,'[' ]

        reverse_pair = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = deque([])

        for p in s:
            if p in openning:
                stack.append(p)
            if p in reverse_pair:
                if stack and reverse_pair[p] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack



        