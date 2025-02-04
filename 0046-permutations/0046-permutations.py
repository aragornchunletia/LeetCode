class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(index):
            
            if index == len(nums):
                res.append(nums[:])
                return

            for i in range(index , len(nums)):
                nums[index] , nums[i] = nums[i] , nums[index]
                helper(index + 1)
                nums[i] , nums[index] = nums[index] , nums[i]

            return

        res = []
        helper(0)
        return res


