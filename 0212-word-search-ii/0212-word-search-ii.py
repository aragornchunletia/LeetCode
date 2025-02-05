from typing import List

class Solution:
    def Trie(self, wordList):
        trie = {}
        for word in wordList:
            temp = trie
            for char in word:
                if char not in temp:
                    temp[char] = {}
                temp = temp[char]
            temp["#"] = True  # Mark the end of a word
        return trie

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = self.Trie(words)

        def dfs(i, j, node, word):
            nonlocal res
            char = board[i][j]
            if char not in node:
                return

            word += char
            node = node[char]

            if "#" in node:
                res.add(word)  

            board[i][j] = "#"  

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] != "#":
                    dfs(x, y, node, word)

            board[i][j] = char  

        res = set()
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")

        return list(res)

