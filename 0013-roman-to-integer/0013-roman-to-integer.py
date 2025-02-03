from collections import deque
class Solution:
    def romanToInt(self, s: str) -> int:
        conv_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        spl_val_dict = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        s = [ c for c in s]
        s = deque(s)
        total = 0

        while s:
            roman = s.popleft()
            spl_char = roman + s[0] if s else None
            if s and spl_char in spl_val_dict:
                total += spl_val_dict[spl_char]
                s.popleft()
            else:
                total += conv_dict[roman]

        return total
