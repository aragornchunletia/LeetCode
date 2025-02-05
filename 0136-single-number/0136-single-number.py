class Solution:
    """
    Xor of equal numbers is zero
    """
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor