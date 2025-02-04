class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        start = len(digits) - 1
        carry = 1

        while start > -1:
            val = digits[start] + carry
            carry = val // 10
            digits[start] = val % 10
            start -= 1

        if carry != 0:
            return [carry] + digits
        return digits