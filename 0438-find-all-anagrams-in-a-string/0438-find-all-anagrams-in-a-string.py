from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_array = [0] * 26
        for char in p:
            p_array[ord(char) - ord('a')] += 1

        
        s_array = [0] * 26
        res = []
        window_size = len(p)

        for i in range(len(s)):

            s_array[ord(s[i]) - ord('a')] += 1

            if i >= window_size:
                s_array[ord(s[i - window_size]) - ord('a')] -= 1

            if s_array == p_array:
                res.append(i - window_size + 1)

        return res
