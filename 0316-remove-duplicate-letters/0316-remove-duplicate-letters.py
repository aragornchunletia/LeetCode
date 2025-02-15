class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occurence = {char : idx for idx,char in enumerate(s)}
        visited = set()
        stack = []

        for i in range(len(s)):
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and last_occurence[stack[-1]] > i:
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])

        return "".join(stack)
