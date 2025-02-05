from typing import List

class Solution:
    """
    Given a list of non-negative integers, arrange them to form the largest possible number.

    Approach:
    - Convert numbers to strings so that we can compare their lexicographical order.
    - Use a bubble sort-like approach to repeatedly swap adjacent elements based on
      their concatenated value to ensure the larger combination comes first.
    - Join the sorted list into a single string.
    - Handle the edge case where the largest number is "0" (e.g., [0,0] should return "0").
    """

    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings for lexicographical comparison
        nums = list(map(str, nums))

        start = 0
        end = len(nums)

        # Bubble sort-like approach to rearrange numbers in the optimal order
        while start < end:
            i = 0
            while i < len(nums) - 1:
                # Swap if concatenating nums[i+1] before nums[i] forms a larger number
                if nums[i] + nums[i + 1] < nums[i + 1] + nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i += 1
            end -= 1  # Reduce the range after each full pass

        # Join the sorted numbers into a single string
        res = "".join(nums)

        # Handle edge case where all numbers are zero (e.g., [0, 0] should return "0")
        return res if res[0] != '0' else '0'
