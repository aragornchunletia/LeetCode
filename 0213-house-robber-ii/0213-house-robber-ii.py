class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return max(nums)

        def helper(arr):
            r_1 = 0
            r_2 = 0
            for i in range(len(arr)):
                temp = max(r_2 + arr[i] , r_1)
                r_2 = r_1
                r_1 = temp
            return r_1

        a1 = helper(nums[:-1])
        a2 = helper(nums[1:])

        return max(a1,a2)
        