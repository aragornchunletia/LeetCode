class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = [0]*26
        start , end = 0 , 0
        n = len(s)
        max_count = 0
        maxL = 0

        while end < len(s):

            idx = ord(s[end]) - ord('A')
            charSet[idx] += 1
            max_count = max(max_count , charSet[idx])

            if end - start - max_count + 1 > k:
                startIdx = ord(s[start]) - ord('A')
                charSet[startIdx] -= 1
                start += 1

            maxL = max(maxL , end - start + 1)
            end += 1

        return maxL