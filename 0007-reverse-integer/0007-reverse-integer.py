class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        sign  = -1 if x < 0 else 1
        x = abs(x)
        number = 0
        while x:

            digit = x % 10
            number = number * 10 + digit
            x = x//10

            if number > MAX or number < sign*number:
                return 0

        return number*sign
        