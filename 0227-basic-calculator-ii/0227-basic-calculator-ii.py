class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")  # Remove spaces
        stack = []
        num = 0
        sign = '+'  # Track the last operator

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build the current number

            # If the character is an operator or the last character in the string
            if char in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # Truncate towards zero
                sign = char  # Update the operator
                num = 0  # Reset the number

        return sum(stack)
