class Solution:
    def longestPalindrome(self, s: str) -> str:
        def middle_out(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        max_len = 0
        maxIdx = (0, 0)
        n = len(s)

        for i in range(n):
            # Odd-length palindrome
            left, right = middle_out(i, i)
            if right - left + 1 > max_len:
                max_len = right - left + 1
                maxIdx = (left, right)

            # Even-length palindrome
            left, right = middle_out(i, i + 1)
            if right - left + 1 > max_len:
                max_len = right - left + 1
                maxIdx = (left, right)

        return s[maxIdx[0]:maxIdx[1] + 1]
