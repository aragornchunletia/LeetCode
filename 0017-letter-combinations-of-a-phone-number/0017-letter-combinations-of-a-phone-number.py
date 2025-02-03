class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        chars = ['abc' , 'def' , 'ghi' , 'jkl' , 'mno' , 'pqrs','tuv','wxyz']

        n = len(digits)
        contention_strings = [chars[int(num) - 2] for num in digits]
        n = len(contention_strings)
        res = []
        def helper(st , i):
            if len(st) == n:
                res.append(st)
                return

            for s in contention_strings[i]:
                helper(st + s , i+1)

        helper("" , 0)

        return res


            
