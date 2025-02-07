class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # To handle negative numbers in 32-bit representation
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # If a is negative, convert it to a 32-bit signed integer
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
