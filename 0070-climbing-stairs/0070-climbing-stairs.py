class Solution:
    # Fibonacci
    def climbStairs(self, n: int) -> int:
        prev = 0
        next = 1
        for i in range(n):
            temp = prev + next
            prev = next
            next = temp
        return next
        