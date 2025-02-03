class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_count = 0
        start = 0

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[end])
            max_count = max(max_count , end - start + 1)

        return max_count


        