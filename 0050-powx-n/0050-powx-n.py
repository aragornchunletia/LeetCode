class Solution:
    def myPow(self, x: float, n: int) -> float:
        # This here is known as fast exponentiation
        #curtails the reccurence tree to logn
        exponent = abs(n)
        def recur(base , exp):
            if exp == 0:
                return 1
            if exp % 2 == 0:
                return recur(base*base , exp//2)
            else:
                return base*recur(base , exp-1)

        ans = recur(x , exponent)
        return (ans)**-1 if n < 0 else ans