class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:
            if char.isalnum() or char == "[":
                stack.append(char)

            elif char == "]":
                st = ""

                while stack and stack[-1] != "[":
                    st = stack.pop() + st

                stack.pop()
                #start of number if the number is to be more than 1 digit
                num = ""
                
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                num = int(num) if num else 1
                stack.append(st*num)

        return "".join(stack)


