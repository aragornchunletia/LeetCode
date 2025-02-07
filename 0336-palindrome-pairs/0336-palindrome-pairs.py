from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Helper function to check if a string is a palindrome
        def ispalindrome(st: str) -> bool:
            return st == st[::-1]
        
        # Create a lookup dictionary mapping reversed words to their indices
        lookup = {word[::-1]: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):  # n+1 to consider empty prefix or suffix
                prefix, suffix = word[:j], word[j:]
                
                # Case 1: If the prefix is a palindrome, check if the reversed suffix exists
                # Example: word = "ab", lookup contains "ba" → ["ba", "ab"] forms a palindrome
                if ispalindrome(prefix) and suffix in lookup and lookup[suffix] != i:
                    result.append([lookup[suffix], i])  # [index of reversed suffix, current word index]
                
                # Case 2: If the suffix is a palindrome, check if the reversed prefix exists
                # Ensures that we don't duplicate cases where j == n (empty suffix)
                if j != n and ispalindrome(suffix) and prefix in lookup and lookup[prefix] != i:
                    result.append([i, lookup[prefix]])  # [current word index, index of reversed prefix]
        
        return result
