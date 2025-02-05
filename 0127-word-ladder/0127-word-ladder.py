from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wSet = set(wordList)
        a_z = "".join([chr(ord('a') + i) for i in range(26)])

        q = deque([(beginWord , 1)])

        while q:
            word , length = q.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                ogChar = word[i]
                for char in a_z:
                    if char == ogChar:
                        continue
                    nextWord = word[0:i] + char + word[i+1:]
                    if nextWord in wSet:
                        q.append((nextWord , length + 1))
                        wSet.remove(nextWord)

        return 0

        

        


