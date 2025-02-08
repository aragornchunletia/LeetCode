class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        maxL = 0
        total = 0
        start  = 0
        sum_dict = {0:-1}

        while start < len(nums):

            total += 1 if nums[start] == 1 else -1

            if total in sum_dict:
                maxL = max(maxL , start - sum_dict[total])
            else:
                sum_dict[total] = start

            start += 1

        return maxL
        